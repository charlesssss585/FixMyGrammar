const inputText = document.getElementById('input-text');
const toneSelect = document.getElementById('tone');
const modeSelect = document.getElementById('mode');
const showComparison = document.getElementById('show-comparison');
const fixButton = document.getElementById('fix-btn');
const outputSection = document.getElementById('output-section');
const correctedOutput = document.getElementById('corrected-output');

fixButton.addEventListener('click', fixGrammar);

function fixGrammar() {
    const text = inputText.value.trim();
    
    if (!text) {
        alert('Please enter some text to fix.');
        return;
    }

    const tone = toneSelect.value;
    const mode = modeSelect.value;
    const comparison = showComparison.checked;

    const corrected = correctText(text, tone, mode);

    displayResult(text, corrected, comparison);
}

function correctText(text, tone, mode) {
    let corrected = text;

    // Step 1: Clean formatting first
    corrected = cleanFormatting(corrected);
    
    // Step 2: Fix spelling and basic grammar
    corrected = fixSpelling(corrected);
    corrected = fixBasicGrammar(corrected);
    
    // Step 3: Fix punctuation
    corrected = fixPunctuation(corrected);
    
    // Step 4: Apply tone adjustments
    if (tone === 'formal') {
        corrected = makeFormal(corrected);
    } else if (tone === 'friendly') {
        corrected = makeFriendly(corrected);
    }

    // Step 5: Apply mode adjustments
    if (mode === 'clarity') {
        corrected = improveClarity(corrected);
    } else if (mode === 'shorten') {
        corrected = shortenText(corrected);
    }
    
    // Step 6: Final capitalization fix
    corrected = fixCapitalization(corrected);

    return corrected;
}

function fixSpelling(text) {
    // Use the dataset for spelling corrections
    for (const [wrong, correct] of Object.entries(GRAMMAR_DATA.spelling)) {
        const pattern = new RegExp(`\\b${wrong}\\b`, 'gi');
        text = text.replace(pattern, correct);
    }
    
    return text;
}

function fixBasicGrammar(text) {
    // Fix capitalization of "I"
    text = text.replace(/\bi\b/g, 'I');
    
    // Fix contractions using dataset
    for (const [wrong, correct] of Object.entries(GRAMMAR_DATA.contractions)) {
        const pattern = new RegExp(`\\b${wrong}\\b`, 'gi');
        text = text.replace(pattern, correct);
    }
    
    // Fix common phrase errors using dataset
    for (const [wrong, correct] of Object.entries(GRAMMAR_DATA.phrases)) {
        const pattern = new RegExp(`\\b${wrong}\\b`, 'gi');
        text = text.replace(pattern, correct);
    }
    
    return text;
}

function fixPunctuation(text) {
    // Fix spacing around punctuation
    text = text.replace(/\s+([.,!?;:])/g, '$1');
    text = text.replace(/([.,!?;:])\s*/g, '$1 ');
    text = text.replace(/\s+/g, ' ');
    
    // Fix quotes
    text = text.replace(/``/g, '"');
    text = text.replace(/''/g, '"');
    
    return text.trim();
}

function fixCapitalization(text) {
    // Capitalize first letter of sentences
    text = text.replace(/(^\w|[.!?]\s+\w)/g, match => match.toUpperCase());
    return text;
}

function cleanFormatting(text) {
    // Remove extra spaces
    text = text.replace(/\s+/g, ' ');
    
    // Remove repeated words
    text = text.replace(/\b(\w+)\s+\1\b/gi, '$1');
    
    // Clean up line breaks
    text = text.replace(/\n{3,}/g, '\n\n');
    
    return text.trim();
}

function makeFormal(text) {
    // Use dataset for formal replacements
    for (const [casual, formal] of Object.entries(GRAMMAR_DATA.formal)) {
        const pattern = new RegExp(`\\b${casual}\\b`, 'gi');
        text = text.replace(pattern, formal);
    }
    
    // Remove exclamation marks for formal tone
    text = text.replace(/!/g, '.');

    return text;
}

function makeFriendly(text) {
    // Use dataset for friendly replacements
    for (const [formal, friendly] of Object.entries(GRAMMAR_DATA.friendly)) {
        const pattern = new RegExp(`\\b${formal}\\b`, 'gi');
        text = text.replace(pattern, friendly);
    }
    
    return text;
}

function improveClarity(text) {
    // Split overly long sentences at conjunctions
    text = text.replace(/,\s+(and|but|so)\s+/gi, '. $1 ');
    
    // Break up run-on sentences
    text = text.replace(/\s+(however|therefore|moreover|furthermore)\s+/gi, '. $1, ');
    
    // Use dataset for clarity improvements
    for (const [complex, simple] of Object.entries(GRAMMAR_DATA.clarity)) {
        const pattern = new RegExp(complex, 'gi');
        text = text.replace(pattern, simple);
    }

    text = fixCapitalization(text);
    return text;
}

function shortenText(text) {
    // Use dataset for shortening replacements
    for (const [long, short] of Object.entries(GRAMMAR_DATA.shorten)) {
        const pattern = new RegExp(long, 'gi');
        text = text.replace(pattern, short);
    }
    
    // Remove filler words using dataset
    GRAMMAR_DATA.fillerWords.forEach(filler => {
        const pattern = new RegExp(`\\b${filler},?\\s+`, 'gi');
        text = text.replace(pattern, '');
    });

    // Condense sentences by removing unnecessary clauses
    text = text.replace(/\b(know|think|believe|feel|say|said|realize)\s+that\s+/gi, '$1 ');
    
    // Combine short sentences into one
    text = text.replace(/\.\s+And\s+/gi, ', and ');
    text = text.replace(/\.\s+But\s+/gi, ', but ');
    text = text.replace(/\.\s+So\s+/gi, ', so ');
    
    // Remove redundant subjects in compound sentences
    text = text.replace(/,\s+and\s+(I|you|he|she|it|we|they)\s+/gi, ' and ');
    
    // Clean up extra spaces from removed words
    text = text.replace(/\s+/g, ' ');
    text = text.replace(/\s+([.,!?;:])/g, '$1');
    text = text.trim();

    return text;
}

function displayResult(original, corrected, showComparison) {
    if (showComparison) {
        correctedOutput.innerHTML = `
            <div class="comparison-container">
                <div class="result-box">
                    <div class="result-title">📌 Before</div>
                    <div class="result-content">${escapeHtml(original)}</div>
                </div>
                <div class="result-box">
                    <div class="result-title">✔ After</div>
                    <div class="result-content">${escapeHtml(corrected)}</div>
                </div>
            </div>
        `;
    } else {
        correctedOutput.innerHTML = `
            <div class="result-box">
                <div class="result-title">✨ Corrected Text</div>
                <div class="result-content">${escapeHtml(corrected)}</div>
            </div>
        `;
    }

    outputSection.classList.remove('hidden');
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
