from transformers import pipeline

# Initialize the summarization pipeline with a pre-trained BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text, max_length=50, min_length=50):
    """
    Summarize the provided text using the BART model.
    
    Parameters:
    - text (str): The text that needs to be summarized.
    - max_length (int): The maximum length of the summary.
    - min_length (int): The minimum length of the summary.

    Returns:
    - str: The summarized version of the text.
    """
    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error in summarization: {str(e)}"