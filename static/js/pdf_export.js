/**
 * PackSense AI - PDF Export, Print & Safe Delete Utilities
 * Works seamlessly within sandboxed iframes and standard browser contexts.
 */

// Function to generate and directly download a pristine PDF file
function downloadReportPDF(elementId, filename, buttonElement) {
  const element = document.getElementById(elementId);
  if (!element) {
    console.error('Element with ID not found:', elementId);
    return;
  }

  let originalBtnText = '';
  if (buttonElement) {
    originalBtnText = buttonElement.innerHTML;
    buttonElement.innerHTML = '⏳ Generating PDF...';
    buttonElement.disabled = true;
    buttonElement.style.opacity = '0.75';
  }

  const opt = {
    margin: [10, 10, 12, 10],
    filename: filename || 'PackSense_Report.pdf',
    image: { type: 'jpeg', quality: 0.98 },
    html2canvas: {
      scale: 2,
      useCORS: true,
      logging: false,
      scrollY: 0
    },
    jsPDF: {
      unit: 'mm',
      format: 'a4',
      orientation: 'portrait'
    },
    pagebreak: { mode: ['avoid-all', 'css', 'legacy'] }
  };

  if (typeof html2pdf !== 'undefined') {
    html2pdf()
      .set(opt)
      .from(element)
      .save()
      .then(function() {
        if (buttonElement) {
          buttonElement.innerHTML = '✅ PDF Saved!';
          setTimeout(function() {
            buttonElement.innerHTML = originalBtnText;
            buttonElement.disabled = false;
            buttonElement.style.opacity = '1';
          }, 2500);
        }
      })
      .catch(function(err) {
        console.warn('html2pdf generation error, falling back to print view:', err);
        if (buttonElement) {
          buttonElement.innerHTML = originalBtnText;
          buttonElement.disabled = false;
          buttonElement.style.opacity = '1';
        }
        try {
          window.print();
        } catch (e) {
          alert('Please use the browser print menu to save as PDF.');
        }
      });
  } else {
    // Fallback if library failed to load
    if (buttonElement) {
      buttonElement.innerHTML = originalBtnText;
      buttonElement.disabled = false;
      buttonElement.style.opacity = '1';
    }
    try {
      window.print();
    } catch (e) {
      console.error('Print unavailable:', e);
    }
  }
}

// Function to handle printing cleanly with iframe resilience
function printReportDocument(elementId, fallbackFilename, buttonElement) {
  try {
    // Attempt standard print
    window.print();
  } catch (err) {
    console.warn('Direct print blocked by iframe sandbox, downloading PDF instead:', err);
    downloadReportPDF(elementId, fallbackFilename, buttonElement);
  }
}

// Safe, non-blocking 2-step delete button handler (replaces iframe-blocked confirm() dialogs)
function armDeleteButton(btn, formId) {
  if (!btn.dataset.armed) {
    btn.dataset.armed = 'true';
    btn.dataset.origText = btn.innerHTML;
    btn.innerHTML = '⚠️ Confirm Delete?';
    btn.style.background = '#dc2626';
    btn.style.color = '#ffffff';
    btn.style.borderColor = '#b91c1c';
    btn.style.fontWeight = '700';

    // Auto-disarm after 4 seconds if user doesn't confirm
    const timer = setTimeout(function() {
      disarmDeleteButton(btn);
    }, 4000);
    btn.dataset.timer = timer;
    return false;
  } else {
    // Second click: submit form or execute deletion
    if (btn.dataset.timer) {
      clearTimeout(parseInt(btn.dataset.timer, 10));
    }
    btn.innerHTML = 'Deleting...';
    btn.disabled = true;
    if (formId) {
      document.getElementById(formId).submit();
    }
    return true;
  }
}

function disarmDeleteButton(btn) {
  btn.dataset.armed = '';
  if (btn.dataset.origText) {
    btn.innerHTML = btn.dataset.origText;
  }
  btn.style.background = '';
  btn.style.color = '';
  btn.style.borderColor = '';
  btn.style.fontWeight = '';
}
