from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data =request.json
        text =data['text']
        vs = analyzer.polarity_scores(text)
        if vs['compound'] >= 0.05:
            return jsonify({'sentiment': 'positive'})
        elif vs['compound'] <= -0.05:
            return jsonify({'sentiment': 'negative'})
        else:
            return jsonify({'sentiment': 'neutral'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)







