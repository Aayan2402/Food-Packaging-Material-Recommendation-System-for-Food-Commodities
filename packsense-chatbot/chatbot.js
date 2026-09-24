/**
 * PackSense AI – Food Safety Assistant
 * Interactive Client Engine
 */

(function () {
  const config = window.PackSenseChatbotConfig || {};
  let chatHistory = [];
  let isAwaitingResponse = false;

  // DOM Elements Cache
  let elements = {};

  function initChatbot() {
    elements = {
      messagesContainer: document.getElementById('chatMessagesScroll'),
      suggestedContainer: document.getElementById('chatSuggestedBar'),
      chatForm: document.getElementById('chatInputForm'),
      chatInput: document.getElementById('chatTextInput'),
      sendBtn: document.getElementById('chatSendBtn'),
      clearBtn: document.getElementById('chatClearBtn'),
      sourcesBtn: document.getElementById('chatSourcesBtn'),
      sourcesModal: document.getElementById('chatSourcesModal'),
      wizardBtn: document.getElementById('chatWizardBtn'),
      wizardModal: document.getElementById('chatWizardModal')
    };

    if (!elements.messagesContainer) return;

    renderSuggestedQuestions();
    attachEventListeners();

    // Initial greeting if chat is empty
    if (elements.messagesContainer.children.length === 0) {
      renderGreetingMessage();
    }

    // Auto-detect and handle query passed from Workspace or PackAudit (?q=...)
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const incomingQuery = urlParams.get('q');
      if (incomingQuery && incomingQuery.trim()) {
        setTimeout(function () {
          if (elements.chatInput) {
            elements.chatInput.value = incomingQuery;
            sendMessage(incomingQuery);
          }
        }, 350);
      }
    } catch (err) {
      console.warn("Could not parse URL query parameters:", err);
    }
  }

  function renderSuggestedQuestions() {
    if (!elements.suggestedContainer || !config.suggestedQuestions) return;
    elements.suggestedContainer.innerHTML = '';
    config.suggestedQuestions.forEach(function (q) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'chat-suggested-btn';
      btn.textContent = q;
      btn.addEventListener('click', function () {
        if (elements.chatInput) {
          elements.chatInput.value = q;
          sendMessage(q);
        }
      });
      elements.suggestedContainer.appendChild(btn);
    });
  }

  function attachEventListeners() {
    if (elements.chatForm) {
      elements.chatForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const text = elements.chatInput.value.trim();
        if (text && !isAwaitingResponse) {
          sendMessage(text);
        }
      });
    }

    if (elements.clearBtn) {
      elements.clearBtn.addEventListener('click', clearChat);
    }

    if (elements.sourcesBtn) {
      elements.sourcesBtn.addEventListener('click', function () {
        openModal(elements.sourcesModal);
      });
    }

    if (elements.wizardBtn) {
      elements.wizardBtn.addEventListener('click', function () {
        openModal(elements.wizardModal);
      });
    }

    // Modal Close Triggers
    document.querySelectorAll('.chat-modal-close, .modal-close-trigger').forEach(function (el) {
      el.addEventListener('click', function () {
        closeAllModals();
      });
    });

    // Close on backdrop click
    document.querySelectorAll('.chat-modal-backdrop').forEach(function (modal) {
      modal.addEventListener('click', function (e) {
        if (e.target === modal) {
          closeAllModals();
        }
      });
    });
  }

  function openModal(modal) {
    if (modal) {
      modal.classList.add('show');
    }
  }

  function closeAllModals() {
    document.querySelectorAll('.chat-modal-backdrop').forEach(function (m) {
      m.classList.remove('show');
    });
  }

  function renderGreetingMessage() {
    const greetingText = `
**PackSense AI – Food Safety Assistant**
Welcome! I provide AI-assisted educational guidance on **Food Packaging, FSSAI regulations, food-grade barrier requirements, and Maharashtra FDA context**.

How can I assist you with your food packaging safety or regulatory inquiries today? You can choose a suggested question above or describe your food item.
    `;
    appendBotMessage(greetingText, false);
  }

  function appendUserMessage(text) {
    const row = document.createElement('div');
    row.className = 'chat-message-row user-msg';
    row.innerHTML = `
      <div class="chat-msg-avatar" title="You">👤</div>
      <div class="chat-bubble">${escapeHtml(text)}</div>
    `;
    elements.messagesContainer.appendChild(row);
    scrollToBottom();
    chatHistory.push({ role: 'user', content: text });
  }

  function appendBotMessage(rawText, isStructured) {
    const row = document.createElement('div');
    row.className = 'chat-message-row bot-msg';

    const formattedContent = formatBotResponse(rawText);

    row.innerHTML = `
      <div class="chat-msg-avatar" title="PackSense AI">🤖</div>
      <div class="chat-bubble">
        ${formattedContent}
        <div class="chat-bubble-actions">
          <button type="button" class="bubble-btn copy-btn" title="Copy response">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span>Copy</span>
          </button>
          <button type="button" class="bubble-btn sources-pop-btn" title="View Official FSSAI/FDA Sources">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
            <span>📚 Official Sources</span>
          </button>
        </div>
      </div>
    `;

    // Attach Copy Handler
    const copyBtn = row.querySelector('.copy-btn');
    if (copyBtn) {
      copyBtn.addEventListener('click', function () {
        navigator.clipboard.writeText(rawText).then(function () {
          copyBtn.querySelector('span').textContent = 'Copied!';
          setTimeout(function () {
            copyBtn.querySelector('span').textContent = 'Copy';
          }, 1800);
        });
      });
    }

    // Attach Sources Handler
    const sourcesBtn = row.querySelector('.sources-pop-btn');
    if (sourcesBtn) {
      sourcesBtn.addEventListener('click', function () {
        openModal(elements.sourcesModal);
      });
    }

    elements.messagesContainer.appendChild(row);
    scrollToBottom();
    chatHistory.push({ role: 'assistant', content: rawText });
  }

  function showTypingIndicator() {
    const id = 'typingIndicatorRow';
    const existing = document.getElementById(id);
    if (existing) return;

    const row = document.createElement('div');
    row.id = id;
    row.className = 'chat-message-row bot-msg';
    row.innerHTML = `
      <div class="chat-msg-avatar">🤖</div>
      <div class="chat-bubble" style="padding: 0.6rem 0.9rem;">
        <div class="typing-dots">
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
        </div>
      </div>
    `;
    elements.messagesContainer.appendChild(row);
    scrollToBottom();
  }

  function removeTypingIndicator() {
    const el = document.getElementById('typingIndicatorRow');
    if (el) el.remove();
  }

  function scrollToBottom() {
    if (elements.messagesContainer) {
      elements.messagesContainer.scrollTop = elements.messagesContainer.scrollHeight;
    }
  }

  function clearChat() {
    if (!elements.messagesContainer) return;
    elements.messagesContainer.innerHTML = '';
    chatHistory = [];
    renderGreetingMessage();
  }

  // Format responses into structured cards if keys are present
  function formatBotResponse(text) {
    if (text.includes('🍱 FOOD') || text.includes('📦 RECOMMENDED PACKAGING')) {
      return renderStructuredCard(text);
    }

    // Markdown-like parser for bold text and lists
    let html = escapeHtml(text);
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\n\n/g, '<br/><br/>');
    html = html.replace(/\n/g, '<br/>');
    return html;
  }

  function renderStructuredCard(rawText) {
    // Parse structured sections
    const lines = rawText.split('\n');
    let currentTag = '';
    let sections = {};

    lines.forEach(function (line) {
      const trimmed = line.trim();
      if (trimmed.startsWith('🍱') || trimmed.includes('FOOD / PRODUCT')) {
        currentTag = 'food';
        sections[currentTag] = (sections[currentTag] || '') + trimmed.replace(/.*FOOD \/ PRODUCT[:\s]*/i, '') + ' ';
      } else if (trimmed.startsWith('📦') || trimmed.includes('RECOMMENDED PACKAGING')) {
        currentTag = 'packaging';
        sections[currentTag] = (sections[currentTag] || '') + trimmed.replace(/.*RECOMMENDED PACKAGING[:\s]*/i, '') + ' ';
      } else if (trimmed.startsWith('🛡️') || trimmed.includes('REQUIRED PROTECTION')) {
        currentTag = 'protection';
        sections[currentTag] = (sections[currentTag] || '') + trimmed.replace(/.*REQUIRED PROTECTION[:\s]*/i, '') + ' ';
      } else if (trimmed.startsWith('🔬') || trimmed.includes('WHY')) {
        currentTag = 'why';
        sections[currentTag] = (sections[currentTag] || '') + trimmed.replace(/.*WHY[:\s]*/i, '') + ' ';
      } else if (trimmed.startsWith('♻️') || trimmed.includes('ALTERNATIVE')) {
        currentTag = 'alternative';
        sections[currentTag] = (sections[currentTag] || '') + trimmed.replace(/.*ALTERNATIVE[:\s]*/i, '') + ' ';
      } else if (trimmed.startsWith('⚠️') || trimmed.includes('FOOD-SAFETY CONSIDERATION')) {
        currentTag = 'safety';
        sections[currentTag] = (sections[currentTag] || '') + trimmed.replace(/.*FOOD-SAFETY CONSIDERATION[:\s]*/i, '') + ' ';
      } else if (trimmed.startsWith('📚') || trimmed.includes('REGULATORY REFERENCE')) {
        currentTag = 'regulatory';
        sections[currentTag] = (sections[currentTag] || '') + trimmed.replace(/.*REGULATORY REFERENCE[:\s]*/i, '') + ' ';
      } else if (trimmed.startsWith('🤖') || trimmed.includes('AI NOTE')) {
        currentTag = 'ainote';
        sections[currentTag] = (sections[currentTag] || '') + trimmed.replace(/.*AI NOTE[:\s]*/i, '') + ' ';
      } else if (currentTag && trimmed) {
        sections[currentTag] = (sections[currentTag] || '') + trimmed + '<br/>';
      }
    });

    let cardHtml = '<div class="structured-response-card">';

    if (sections.food) {
      cardHtml += `
        <div class="structured-section food-header">
          <span class="section-label">🍱 FOOD / PRODUCT</span>
          ${sections.food}
        </div>
      `;
    }

    if (sections.packaging) {
      cardHtml += `
        <div class="structured-section recommended-pack">
          <span class="section-label">📦 RECOMMENDED PACKAGING</span>
          ${sections.packaging}
        </div>
      `;
    }

    if (sections.protection) {
      cardHtml += `
        <div class="structured-section protection-req">
          <span class="section-label">🛡️ REQUIRED PROTECTION</span>
          ${sections.protection}
        </div>
      `;
    }

    if (sections.why) {
      cardHtml += `
        <div class="structured-section why-suitable">
          <span class="section-label">🔬 WHY IT IS SUITABLE</span>
          ${sections.why}
        </div>
      `;
    }

    if (sections.alternative) {
      cardHtml += `
        <div class="structured-section alternative-mat">
          <span class="section-label">♻️ ALTERNATIVE MATERIALS</span>
          ${sections.alternative}
        </div>
      `;
    }

    if (sections.safety) {
      cardHtml += `
        <div class="structured-section food-safety-warn">
          <span class="section-label">⚠️ IMPORTANT FOOD-SAFETY CONSIDERATIONS</span>
          ${sections.safety}
        </div>
      `;
    }

    if (sections.regulatory) {
      cardHtml += `
        <div class="structured-section reg-reference">
          <span class="section-label">📚 REGULATORY REFERENCE & BIS STANDARDS</span>
          ${sections.regulatory}
        </div>
      `;
    }

    cardHtml += `
      <div class="structured-section ai-note">
        <span class="section-label">🤖 AI NOTE (PRELIMINARY RECOMMENDATION)</span>
        ${sections.ainote || 'AI-Assisted Preliminary Recommendation. Verify current standards before commercial deployment.'}
      </div>
    `;

    cardHtml += '</div>';
    return cardHtml;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Core Send Logic
  async function sendMessage(text) {
    if (!text) return;
    appendUserMessage(text);
    if (elements.chatInput) elements.chatInput.value = '';

    isAwaitingResponse = true;
    if (elements.sendBtn) elements.sendBtn.disabled = true;
    showTypingIndicator();

    try {
      const response = await fetch(config.apiEndpoint || '/api/chatbot/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: text,
          history: chatHistory.slice(-6)
        })
      });

      if (!response.ok) {
        throw new Error('API server returned status: ' + response.status);
      }

      const data = await response.json();
      removeTypingIndicator();
      appendBotMessage(data.reply || data.response || 'Information retrieved.', true);
    } catch (err) {
      console.warn('Backend API request error, utilizing client-side knowledge fallback:', err);
      removeTypingIndicator();
      const fallbackReply = generateKnowledgeFallback(text);
      appendBotMessage(fallbackReply, true);
    } finally {
      isAwaitingResponse = false;
      if (elements.sendBtn) elements.sendBtn.disabled = false;
      if (elements.chatInput) elements.chatInput.focus();
    }
  }

  // Client-Side Knowledge Base Fallback when offline/network failure
  function generateKnowledgeFallback(query) {
    const q = query.toLowerCase();

    // 1. Newspaper Question
    if (q.includes('newspaper') || q.includes('news paper') || q.includes('wrap')) {
      return `
**🍱 FOOD / PRODUCT**: Cooked street foods, fried snacks, bakery, fresh produce
**📦 RECOMMENDED PACKAGING**: Food-grade Greaseproof Paper (IS 6615), Butter paper, or clean plant leaf wraps
**🛡️ REQUIRED PROTECTION**: Barrier against oil strike-through and zero toxic chemical migration
**🔬 WHY**: Newspaper printing inks contain carcinogenic mineral oil aromatic hydrocarbons (MOAH), lead, cadmium, and naphthylamines. Hot and oily food leaches these solvents within seconds, posing severe cancer and toxicity risks.
**♻️ ALTERNATIVE**: Food-grade stainless steel plates, certified parchment paper, or fresh banana leaves
**⚠️ FOOD-SAFETY CONSIDERATION**: Regulation 3(4) of Food Safety and Standards (Packaging) Regulations, 2018 strictly bans using newspaper for wrapping, storing, or absorbing oil from food.
**📚 REGULATORY REFERENCE**: FSSAI Packaging Regulations 2018; BIS IS 6615; Maharashtra FDA public advisory notifications.
**🤖 AI NOTE**: AI-Assisted Preliminary Recommendation. Newspaper must NEVER be used for food contact under any circumstance.
      `;
    }

    // 2. Food Grade Packaging Definition
    if (q.includes('food-grade') || q.includes('food grade') || q.includes('what is food grade')) {
      return `
**🍱 FOOD / PRODUCT**: Universal Food Contact Materials
**📦 RECOMMENDED PACKAGING**: Materials certified under Indian Standards (e.g., IS 10146 for PE, IS 10910 for PP, IS 1382 for Glass, IS 1997 for Tinplate)
**🛡️ REQUIRED PROTECTION**: Chemical inertness and compliance with Overall Migration Limit (< 60 mg/kg under IS 9845)
**🔬 WHY**: Food-grade indicates that the material has been formulated and tested to ensure zero transfer of harmful monomers, heavy metals, or plasticizers that could endanger consumer health or degrade food aroma/taste.
**♻️ ALTERNATIVE**: Type III Neutral Soda-Lime Glass or Food-Grade Stainless Steel (SS304/SS316)
**⚠️ FOOD-SAFETY CONSIDERATION**: Recycled untreated plastics are strictly prohibited in primary food packaging under Regulation 3(2) of FSSAI Packaging Regulations 2018.
**📚 REGULATORY REFERENCE**: FSSAI Packaging Regulations, 2018; IS 9845:2020 migration standards.
**🤖 AI NOTE**: AI-Assisted Preliminary Recommendation. Verify migration certificates from manufacturer prior to procurement.
      `;
    }

    // 3. Oily / Fatty Foods
    if (q.includes('oily') || q.includes('fat') || q.includes('fried') || q.includes('chips')) {
      return `
**🍱 FOOD / PRODUCT**: Oily Foods, Fried Namkeen, Potato Chips, Roasted Nuts
**📦 RECOMMENDED PACKAGING**: Metallized BOPP / Polyethylene multi-layer laminate with Nitrogen (N₂) gas flushing
**🛡️ REQUIRED PROTECTION**: Ultra-high oxygen barrier (OTR < 15 cc/m²/day), zero light transmission, and grease resistance
**🔬 WHY**: Unsaturated fats undergo rapid lipid peroxidation when exposed to atmospheric oxygen and light, producing rancid off-flavors (hexanals). Metallized film completely blocks UV light and oxygen.
**♻️ ALTERNATIVE**: Food-grade Greaseproof Paper (IS 6615) with bio-wax coating for short-duration shelf life
**⚠️ FOOD-SAFETY CONSIDERATION**: Never pack hot fried snacks directly into low-grade polyethylene bags; high oil temperatures accelerate plasticizer migration.
**📚 REGULATORY REFERENCE**: FSSAI Packaging Regulations, 2018 (Schedule I: IS 10910, IS 1060).
**🤖 AI NOTE**: AI-Assisted Preliminary Recommendation. Nitrogen flush with < 2% residual O₂ extends shelf life by 400%.
      `;
    }

    // 4. Milk
    if (q.includes('milk') || q.includes('dairy')) {
      return `
**🍱 FOOD / PRODUCT**: Fresh Pasteurized or Long-Life (UHT) Milk
**📦 RECOMMENDED PACKAGING**: 3/5-layer co-extruded LDPE/LLDPE pouch with carbon-black UV barrier (pasteurized) or 6-layer Aseptic Brick Carton (UHT)
**🛡️ REQUIRED PROTECTION**: Complete light barrier (blocks riboflavin breakdown), airtight seal, microbial sterility
**🔬 WHY**: Milk contains Vitamin B2 (riboflavin), which is a photosensitizer. Exposure to daylight triggers riboflavin photolysis within 2 hours, resulting in oxidized cardboard off-flavor and nutrient loss.
**♻️ ALTERNATIVE**: Type III Amber Glass bottles or HDPE bottles with UV inhibitors
**⚠️ FOOD-SAFETY CONSIDERATION**: Cold-chain maintenance (<= 4°C) is mandatory for pasteurized pouches to prevent rapid bacterial spoilage.
**📚 REGULATORY REFERENCE**: FSSAI Packaging Regulations, 2018; IS 10146 (PE for food contact).
**🤖 AI NOTE**: AI-Assisted Preliminary Recommendation. Maintain tamper-evident closures on all consumer units.
      `;
    }

    // 5. Maharashtra FDA & Tukaram Munde Context
    if (q.includes('tukaram') || q.includes('munde') || q.includes('maharashtra fda') || q.includes('fda')) {
      return `
**🍱 FOOD / PRODUCT**: Regulatory Administration & State Enforcement
**📦 RECOMMENDED PACKAGING**: FSSAI-compliant certified packaging
**🛡️ REQUIRED PROTECTION**: Institutional demarcation between Union statutory regulation and State administrative enforcement
**🔬 WHY**: These requirements arise from the applicable FSSAI/Government regulatory framework. Maharashtra FDA enforcement and public food-safety activities during the relevant period can be discussed separately.
**♻️ ALTERNATIVE**: N/A (Statutory framework)
**⚠️ FOOD-SAFETY CONSIDERATION**: During his tenure as Commissioner of FDA Maharashtra (late 2022 to early 2023), Tukaram Munde led intensive statewide crackdowns on adulterated milk, spurious festive mawa/khoya, loose unbranded edible oils, and non-compliant food packaging. Note: FSSAI formulates the national packaging regulations, while Maharashtra FDA enforces them at state level.
**📚 REGULATORY REFERENCE**: Food Safety and Standards Act, 2006; Maharashtra FDA Department Orders.
**🤖 AI NOTE**: AI-Assisted Educational Context. If a specific enforcement detail cannot be verified from an official government gazette, the assistant notes: "I could not verify this claim from an official source."
      `;
    }

    // Default Fallback
    return `
**🍱 FOOD / PRODUCT**: Food Commodity (${escapeHtml(query)})
**📦 RECOMMENDED PACKAGING**: Food-Grade Inert Multi-layer Laminate or Certified Paperboard
**🛡️ REQUIRED PROTECTION**: Barrier tailored to moisture, oxygen, light, and temperature conditions
**🔬 WHY**: Packaging must preserve freshness, prevent microbial contamination, and comply with FSSAI limits.
**♻️ ALTERNATIVE**: Type III Soda-Lime Glass or Biodegradable Paperboard with Bio-Wax Coating
**⚠️ FOOD-SAFETY CONSIDERATION**: Ensure the packaging material complies with the Overall Migration Limit of 60 mg/kg under IS 9845.
**📚 REGULATORY REFERENCE**: Food Safety and Standards (Packaging) Regulations, 2018.
**🤖 AI NOTE**: AI-Assisted Preliminary Recommendation. Use the 12-factor wizard for a granular barrier analysis.
    `;
  }

  // Interactive Recommendation Wizard Submission
  window.submitPackSenseWizard = async function (e) {
    if (e) e.preventDefault();
    const form = document.getElementById('chatWizardForm');
    if (!form) return;

    const formData = new FormData(form);
    const payload = {};
    formData.forEach((val, key) => { payload[key] = val; });

    closeAllModals();

    const summaryPrompt = `Recommend safe packaging for: ${payload.foodName || 'Food Item'}, Moisture: ${payload.moistureLevel}, Fat/Oil: ${payload.fatContent}, Acidity: ${payload.acidity}, Oxygen Sensitivity: ${payload.oxygenSensitivity}, Light Sensitivity: ${payload.lightSensitivity}, Storage: ${payload.storageCondition}, Sustainability: ${payload.sustainability}`;

    sendMessage(summaryPrompt);
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChatbot);
  } else {
    initChatbot();
  }
})();
