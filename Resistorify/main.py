from flask import Flask, render_template, request, jsonify
from flask import render_template

app = Flask(__name__)

COLOR_INFO = {
    'black': {'digit': 0, 'multiplier': 1, 'tolerance': None, 'ppm': None},
    'brown': {'digit': 1, 'multiplier': 10, 'tolerance': 1, 'ppm': 100},
    'red': {'digit': 2, 'multiplier': 100, 'tolerance': 2, 'ppm': 50},
    'orange': {'digit': 3, 'multiplier': 1000, 'tolerance': 3, 'ppm': 15},
    'yellow': {'digit': 4, 'multiplier': 10000, 'tolerance': 4, 'ppm': 25},
    'green': {'digit': 5, 'multiplier': 100000, 'tolerance': 0.5, 'ppm': None},
    'blue': {'digit': 6, 'multiplier': 1000000, 'tolerance': 0.25, 'ppm': 10},
    'violet': {'digit': 7, 'multiplier': 10000000, 'tolerance': 0.10, 'ppm': 5},
    'gray': {'digit': 8, 'multiplier': 100000000, 'tolerance': 0.05, 'ppm': None},
    'white': {'digit': 9, 'multiplier': 1000000000, 'tolerance': None, 'ppm': None}
}

GOLD_SILVER_INFO = {
    'gold': {'digit': None, 'multiplier': 0.1, 'tolerance': 5, 'ppm': None},
    'silver': {'digit': None, 'multiplier': 0.01, 'tolerance': 10, 'ppm': None}
}

def calculate_resistance(bands, num_bands):
    try:
        band_info = []

        for band in bands:
            if band.lower() in COLOR_INFO:
                band_info.append(COLOR_INFO[band.lower()])
            elif band.lower() in GOLD_SILVER_INFO:
                band_info.append(GOLD_SILVER_INFO[band.lower()])
            else:
                return None

        digit_values = [info['digit'] for info in band_info if info['digit'] is not None]
        multiplier_values = [info['multiplier'] for info in band_info if info['multiplier'] is not None]

        if None in digit_values:
            resistance = None
        elif num_bands == 3:
            resistance = digit_values[0] * 10 ** digit_values[1]
        elif num_bands == 4:
            resistance = (digit_values[0] * 10 + digit_values[1]) * 10 ** digit_values[2]
        elif num_bands == 5:
            resistance = (digit_values[0] * 100 + digit_values[1] * 10 + digit_values[2]) * 10 ** digit_values[3]
        elif num_bands == 6:
            resistance = (digit_values[0] * 100 + digit_values[1] * 10 + digit_values[2]) * 10 ** digit_values[3] + digit_values[3] * multiplier_values[1]
        else:
            resistance = None

        return resistance

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
@app.route('/')
def index():
    return render_template('test.html')

@app.route('/calculate_resistance/<int:num_bands>', methods=['POST'])
def calculate_resistance_api(num_bands):
    try:
        data = request.json
        bands = data['bands']
        result = calculate_resistance(bands, num_bands)

        if result is not None:
            return jsonify({'resistance': result}), 200
        else:
            return jsonify({'error': 'Invalid input or incomplete color combination'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
