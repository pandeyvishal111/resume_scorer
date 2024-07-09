from flask import Flask, request, jsonify
from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F

app = Flask(__name__)

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

@app.route('/score', methods=['POST'])
def score():
    data = request.get_json()
    job_description = data.get('job_description')
    resume = data.get('resume')

    if not job_description or not resume:
        return jsonify({'error': 'Job description and resume are required'}), 400

    try:
        score = get_relevance_score(job_description, resume)
        return jsonify({'score': score})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_relevance_score(job_description, resume):
    job_description_inputs = tokenizer(job_description, return_tensors='pt', truncation=True, padding='max_length', max_length=512)
    resume_inputs = tokenizer(resume, return_tensors='pt', truncation=True, padding='max_length', max_length=512)
    
    with torch.no_grad():
        job_description_outputs = model(**job_description_inputs)
    with torch.no_grad():
        resume_outputs = model(**resume_inputs)
    
    job_description_embedding = job_description_outputs.last_hidden_state[:, 0, :]
    resume_embedding = resume_outputs.last_hidden_state[:, 0, :]
    
    similarity = F.cosine_similarity(job_description_embedding, resume_embedding, dim=1).item()
    score = (similarity + 1) * 50  # similarity ranges from -1 to 1, so convert it to 0-100
    return score

if __name__ == '__main__':
    app.run(debug=True)
