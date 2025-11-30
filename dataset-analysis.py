#!/usr/bin/env python3
"""
English Spelling Corrections Dataset Analysis
Demonstrates various ways to analyze and use the spelling corrections dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

def load_and_explore_dataset(filename='spelling-corrections-dataset.csv'):
    """Load the dataset and perform basic exploration"""
    
    # Load the dataset
    df = pd.read_csv(filename)
    
    print("=== Dataset Overview ===")
    print(f"Total records: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print(f"Memory usage: {df.memory_usage().sum()} bytes")
    
    print("\n=== Sample Data ===")
    print(df.head(10))
    
    print("\n=== Error Type Distribution ===")
    error_counts = df['error_type'].value_counts()
    print(error_counts)
    
    print("\n=== Frequency Category Distribution ===")
    freq_counts = df['frequency_category'].value_counts()
    print(freq_counts)
    
    return df

def analyze_error_patterns(df):
    """Analyze common patterns in spelling errors"""
    
    print("\n=== Error Pattern Analysis ===")
    
    # Length differences
    df['length_diff'] = df['correct_word'].str.len() - df['incorrect_word'].str.len()
    
    print("Length differences (correct - incorrect):")
    print(df['length_diff'].value_counts().sort_index())
    
    # Most common incorrect words
    print("\nMost frequently misspelled words:")
    common_errors = df['incorrect_word'].value_counts().head(10)
    print(common_errors)
    
    # Analyze by word length
    df['word_length'] = df['correct_word'].str.len()
    print("\nError distribution by word length:")
    length_analysis = df.groupby('word_length')['error_type'].count().sort_index()
    print(length_analysis)

def create_spelling_corrector(df):
    """Create a simple spelling corrector from the dataset"""
    
    # Create correction dictionary
    corrections = dict(zip(df['incorrect_word'], df['correct_word']))
    
    def correct_text(text):
        """Apply spelling corrections to text"""
        words = text.split()
        corrected_words = []
        
        for word in words:
            # Remove punctuation for matching
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            if clean_word in corrections:
                # Preserve original capitalization and punctuation
                corrected = corrections[clean_word]
                if word[0].isupper():
                    corrected = corrected.capitalize()
                
                # Add back punctuation
                punct = re.findall(r'[^\w]', word)
                if punct:
                    corrected += ''.join(punct)
                
                corrected_words.append(corrected)
            else:
                corrected_words.append(word)
        
        return ' '.join(corrected_words)
    
    return correct_text

def generate_training_data(df, test_size=0.2):
    """Generate training and test sets for ML models"""
    
    from sklearn.model_selection import train_test_split
    
    # Prepare features and labels
    X = df['incorrect_word'].values
    y = df['correct_word'].values
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, 
        stratify=df['error_type']
    )
    
    print(f"\n=== Training Data Split ===")
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    
    return X_train, X_test, y_train, y_test

def visualize_data(df):
    """Create visualizations of the dataset"""
    
    # Set up the plotting style
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Error type distribution
    error_counts = df['error_type'].value_counts()
    axes[0, 0].bar(range(len(error_counts)), error_counts.values)
    axes[0, 0].set_xticks(range(len(error_counts)))
    axes[0, 0].set_xticklabels(error_counts.index, rotation=45, ha='right')
    axes[0, 0].set_title('Distribution of Error Types')
    axes[0, 0].set_ylabel('Count')
    
    # Frequency category distribution
    freq_counts = df['frequency_category'].value_counts()
    axes[0, 1].pie(freq_counts.values, labels=freq_counts.index, autopct='%1.1f%%')
    axes[0, 1].set_title('Frequency Category Distribution')
    
    # Word length distribution
    df['word_length'] = df['correct_word'].str.len()
    axes[1, 0].hist(df['word_length'], bins=15, alpha=0.7, edgecolor='black')
    axes[1, 0].set_title('Distribution of Word Lengths')
    axes[1, 0].set_xlabel('Word Length (characters)')
    axes[1, 0].set_ylabel('Count')
    
    # Length difference analysis
    df['length_diff'] = df['correct_word'].str.len() - df['incorrect_word'].str.len()
    axes[1, 1].hist(df['length_diff'], bins=10, alpha=0.7, edgecolor='black')
    axes[1, 1].set_title('Length Difference (Correct - Incorrect)')
    axes[1, 1].set_xlabel('Character Difference')
    axes[1, 1].set_ylabel('Count')
    
    plt.tight_layout()
    plt.savefig('spelling_dataset_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def export_for_ml_frameworks(df):
    """Export data in formats suitable for different ML frameworks"""
    
    # For TensorFlow/Keras
    tf_data = {
        'source': df['incorrect_word'].tolist(),
        'target': df['correct_word'].tolist(),
        'error_type': df['error_type'].tolist()
    }
    
    import json
    with open('spelling_data_tensorflow.json', 'w') as f:
        json.dump(tf_data, f, indent=2)
    
    # For PyTorch (TSV format)
    pytorch_df = df[['incorrect_word', 'correct_word']].copy()
    pytorch_df.to_csv('spelling_data_pytorch.tsv', sep='\t', index=False, header=False)
    
    # For Hugging Face transformers
    hf_df = df.copy()
    hf_df['input_text'] = 'correct: ' + hf_df['incorrect_word']
    hf_df['target_text'] = hf_df['correct_word']
    hf_df[['input_text', 'target_text']].to_csv('spelling_data_huggingface.csv', index=False)
    
    print("Exported data for ML frameworks:")
    print("- TensorFlow: spelling_data_tensorflow.json")
    print("- PyTorch: spelling_data_pytorch.tsv")
    print("- Hugging Face: spelling_data_huggingface.csv")

def main():
    """Main analysis pipeline"""
    
    print("English Spelling Corrections Dataset Analysis")
    print("=" * 50)
    
    # Load and explore the dataset
    df = load_and_explore_dataset()
    
    # Analyze error patterns
    analyze_error_patterns(df)
    
    # Create a simple spelling corrector
    corrector = create_spelling_corrector(df)
    
    # Test the corrector
    test_text = "I recieve alot of emails with spelling erors that need to be seperate."
    corrected = corrector(test_text)
    print(f"\n=== Spelling Correction Demo ===")
    print(f"Original:  {test_text}")
    print(f"Corrected: {corrected}")
    
    # Generate training data
    X_train, X_test, y_train, y_test = generate_training_data(df)
    
    # Create visualizations
    visualize_data(df)
    
    # Export for ML frameworks
    export_for_ml_frameworks(df)
    
    print("\n=== Analysis Complete ===")
    print("Check the generated files for ML-ready data formats!")

if __name__ == "__main__":
    main()