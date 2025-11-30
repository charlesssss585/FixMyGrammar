# English Spelling Corrections Dataset

## Overview
This dataset contains 300+ common English spelling errors paired with their correct spellings, extracted from a real-world grammar correction application. The dataset is designed for training spelling correction models, analyzing common spelling patterns, and building educational tools.

## Dataset Description
- **Total Records**: 300+ spelling correction pairs
- **Format**: CSV with headers
- **Source**: Curated from common spelling mistakes in digital communication
- **Use Cases**: NLP, spell checkers, educational applications, error analysis

## Column Descriptions

| Column | Type | Description |
|--------|------|-------------|
| `incorrect_word` | String | The misspelled word as commonly typed |
| `correct_word` | String | The correct spelling of the word |
| `error_type` | Category | Classification of the spelling error type |
| `frequency_category` | Category | How commonly this error occurs |

## Error Type Categories

1. **missing_vowel**: Missing vowel letters (e.g., "definatly" → "definitely")
2. **missing_consonant**: Missing consonant letters (e.g., "begining" → "beginning")
3. **vowel_order**: Incorrect vowel sequence (e.g., "recieve" → "receive")
4. **vowel_substitution**: Wrong vowel used (e.g., "seperate" → "separate")
5. **consonant_substitution**: Wrong consonant used (e.g., "advise" → "advice")
6. **double_consonant**: Incorrect consonant doubling (e.g., "accross" → "across")
7. **letter_order**: Letters in wrong sequence (e.g., "thier" → "their")
8. **extra_vowel**: Unnecessary vowel added (e.g., "arguement" → "argument")
9. **word_separation**: Incorrect word boundaries (e.g., "alot" → "a lot")
10. **missing_apostrophe**: Missing apostrophe in contractions (e.g., "dont" → "don't")
11. **word_confusion**: Confused with similar word (e.g., "defiantly" → "definitely")

## Frequency Categories

- **very_common**: Errors seen frequently in everyday writing
- **common**: Regular spelling mistakes
- **uncommon**: Less frequent but notable errors
- **rare**: Infrequent spelling mistakes

## Potential Applications

### Machine Learning
- Training data for spelling correction models
- Feature engineering for NLP pipelines
- Error pattern analysis and classification

### Educational Technology
- Adaptive spelling tutors
- Error-specific feedback systems
- Difficulty assessment tools

### Linguistic Research
- Phonetic error analysis
- Cognitive spelling studies
- Error pattern evolution research

### Software Development
- Spell checker improvement
- Autocorrect algorithm training
- Grammar checking applications

## Data Quality Notes

- All entries manually verified for accuracy
- Includes both phonetic and visual similarity errors
- Covers various difficulty levels and word types
- Balanced representation across error categories

## Usage Examples

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('spelling-corrections-dataset.csv')

# Analyze error types
error_distribution = df['error_type'].value_counts()
print(error_distribution)

# Filter by frequency
common_errors = df[df['frequency_category'] == 'very_common']

# Create training pairs
X = df['incorrect_word'].values
y = df['correct_word'].values
```

## License
This dataset is released under Creative Commons Attribution 4.0 International License.

## Citation
If you use this dataset in your research, please cite:
```
English Spelling Corrections Dataset (2024)
Grammar Checker Application Data
Available at: [Your Kaggle Profile]
```

## Acknowledgments
Data compiled from real-world spelling correction applications and common error patterns observed in digital communication platforms.