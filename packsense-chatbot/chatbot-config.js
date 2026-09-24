/**
 * PackSense AI – Food Safety Assistant
 * Configuration and Knowledge Base Integrations
 */

window.PackSenseChatbotConfig = {
  name: "🤖 PackSense AI – Food Safety Assistant",
  subtitle: "Ask about Food Packaging, FSSAI & FDA Food-Safety Requirements",
  apiEndpoint: "/api/chatbot/query",
  recommendEndpoint: "/api/chatbot/recommend",
  disclaimer: "PackSense AI provides AI-assisted educational information and preliminary food-packaging recommendations. It is not an official FSSAI or Maharashtra FDA system and does not provide regulatory approval, certification or legal advice. Always verify applicable regulations and food-contact requirements using current official sources before making commercial packaging decisions.",
  suggestedQuestions: [
    "What is food-grade packaging?",
    "Can newspaper be used to wrap food?",
    "What packaging is suitable for oily food?",
    "What packaging is suitable for milk?",
    "What packaging is suitable for spices?",
    "What packaging is suitable for dry food?",
    "How does packaging affect shelf life?",
    "What are FSSAI packaging requirements?",
    "What does Maharashtra FDA do?",
    "What is the Tukaram Munde FDA context?",
    "Which packaging material is suitable for my food?",
    "How can I select safe food packaging?"
  ],
  officialSources: [
    {
      name: "FSSAI Packaging Regulations, 2018 (Official Gazette)",
      url: "https://www.fssai.gov.in/upload/uploadfiles/files/Gazette_Notification_Packaging_24_12_2018.pdf",
      description: "Statutory regulations prohibiting newspaper and prescribing BIS standards for food-contact materials."
    },
    {
      name: "Food Safety and Standards Act, 2006 (Act 34 of 2006)",
      url: "https://www.fssai.gov.in/cms/food-safety-and-standards-act-2006.php",
      description: "The primary national parliamentary legislation establishing FSSAI and food safety administration in India."
    },
    {
      name: "Maharashtra Food and Drug Administration (FDA) Portal",
      url: "https://fda.maharashtra.gov.in",
      description: "Official portal of Food and Drug Administration, Maharashtra State for licensing, inspections, and enforcement."
    },
    {
      name: "IS 9845:2020 Plastics Migration Standards (BIS)",
      url: "https://standardsbis.bsbedge.com",
      description: "Indian Standard method of analysis for determination of overall and specific migration limits."
    }
  ],
  wizardSteps: [
    { id: "foodName", label: "What is your food or product?", placeholder: "e.g., Potato Chips, Fresh Paneer, Alphonso Mango, Ground Spices" },
    { id: "moistureLevel", label: "Moisture Level", options: ["Dry (< 10%)", "Semi-moist (10-40%)", "High moisture / liquid (> 50%)"] },
    { id: "fatContent", label: "Fat / Oil Content", options: ["Zero / Negligible", "Moderate (5-15%)", "High fat / fried (> 20%)"] },
    { id: "acidity", label: "Acidity / pH", options: ["Neutral (pH 6-7)", "Mildly acidic (pH 4.5-6)", "High acid / Pickled (pH < 4.5)"] },
    { id: "oxygenSensitivity", label: "Oxygen Sensitivity", options: ["Low", "Moderate", "Extremely High (Oxidizes/Rancid)"] },
    { id: "lightSensitivity", label: "Light Sensitivity", options: ["Not sensitive", "Moderate", "High (Photolysis / UV degradation)"] },
    { id: "storageCondition", label: "Storage Condition", options: ["Ambient Room Temp", "Cold Chain (0-4°C)", "Frozen (-18°C)"] },
    { id: "sustainability", label: "Sustainability Preference", options: ["Standard High-Barrier", "Down-gauged Recycled Content", "100% Compostable / Bio-based"] }
  ]
};
