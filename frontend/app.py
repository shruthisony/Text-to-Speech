import gradio as gr
import requests
API_URL = "http://127.0.0.1:8000/analyze"
def analyze_company(company):
    try:
        response = requests.post(API_URL, params={"company": company})
        data = response.json()
        if "error" in data:
            return "Error: " + data["error"], None
        text_output = f"*Summary for {company}*\n\n"
        for i, article in enumerate(data["articles"], 1):
            text_output += f"*{i}. {article['title']}*\n"
            text_output += f"Link [Read more]({article['link']})\n\n"
            text_output += f"Summary: {article['summary']}\n"
            text_output += f"Sentiment: {article['sentiment']}\n"
            text_output += f"Topics: {', '.join(article.get('topics', []))}\n\n"
        text_output += f"*Final Summary:* {data.get('summary', '')}\n\n"
        sentiment_counts = data.get("sentiment_distribution", {})
        if sentiment_counts:
            text_output += "*Sentiment Distribution:*\n"
            for sentiment, count in sentiment_counts.items():
                text_output += f"- {sentiment}: {count}\n"
        insights = data.get("insights")
        if insights:
            text_output += f"\n*Insights:* {insights}\n"
        return text_output, data["audio"]
    except Exception as e:
        return f"Error: {str(e)}", None
with gr.Blocks() as demo:
    gr.Markdown("## News Summarizer")
    company_input = gr.Textbox(label="Enter Company Name", value="Tesla")
    analyze_btn = gr.Button(" Analyze")
    output_text = gr.Markdown()
    audio_output = gr.Audio(label="Hindi Audio Summary")
    analyze_btn.click(fn=analyze_company, inputs=company_input, outputs=[output_text, audio_output])
demo.launch()
