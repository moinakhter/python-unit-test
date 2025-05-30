# NLP Service Testing | UnitTest

## Overview

This repository contains a unit testing suite for NLP services powered by BERT and RoBERTa models. The tests validate the intent recognition and slot filling capabilities of these models for various user inputs in a conversational AI system. The suite integrates with six additional services within the broader system, which are assumed to handle complementary tasks such as data processing, storage, or external API interactions.

## Project Structure

- **services/nlp/bert/bert.py**: Implementation of the BERT model for NLP tasks.
- **services/nlp/roberta/roberta.py**: Implementation of the RoBERTa model for NLP tasks.
- **tests/test_nlp_service.py**: Unit tests for validating BERT and RoBERTa model predictions.

## Prerequisites

- Python 3.8 or higher
- Required Python packages (listed in `requirements.txt`):
  - `transformers` (for BERT and RoBERTa models)
  - Other dependencies specific to the models and services
- Access to the six additional services integrated into the system
- Pre-trained BERT and RoBERTa models configured in test mode

## Installation

1. Clone or download the repository.
2. Navigate to the project directory and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the six additional services are properly configured and accessible.
4. Verify that the BERT and RoBERTa models are set up in test mode and accessible via the `services/nlp` directory.

## Usage

Run the unit tests using the following command:

```bash
python -m unittest tests/test_nlp_service.py
```

The test suite will:
1. Initialize BERT and RoBERTa models in test mode.
2. Run six test cases (three for each model) to validate intent and slot predictions.
3. Output test results, indicating whether the predicted slots match the expected slots for each input.

## Unit Testing

The unit testing suite is implemented in `tests/test_nlp_service.py` using Python's `unittest` framework. It tests the following:

- **Test Cases**:
  - **test_01**: Tests BERT model with input "Nasilsin" (smalltalk).
  - **test_02**: Tests BERT model with input "italya'da sicaklik nedir" (city, weather request).
  - **test_03**: Tests BERT model with input "bitcoin fiyatı" (question text).
  - **test_04**: Tests RoBERTa model with input "naptin" (smalltalk).
  - **test_05**: Tests RoBERTa model with input "dolar ne kadar" (question text).
  - **test_06**: Tests RoBERTa model with input "i want to chat" (chat).

- **Test Logic**:
  - Each test sends a user input to the respective model (BERT or RoBERTa) and retrieves the predicted intent and slots.
  - The predicted slots are compared against expected slots using `assertListEqual`.
  - The tests ensure that the models correctly identify intents and extract relevant slots from user inputs.

- **Input Template**:
  - The suite formats inputs for each model using specific channel names (`bert_model_input` for BERT, `roberta_model_input` for RoBERTa).
  - The input structure includes `type`, `pattern`, `channel`, and `data` fields.

- **Running Tests**:
  - Tests are executed via the `unittest` framework, with results displayed in the console.
  - To run specific tests, use:
    ```bash
    python -m unittest tests.test_nlp_service.NlpServiceTest.test_01
    ```

## Integration with Other Services

The testing suite assumes integration with six additional services within the system. These services are not detailed in the provided code but are expected to be accessible via the project’s root directory (added to `sys.path`). Ensure these services are properly configured and running before executing the tests.

## Notes

- The BERT and RoBERTa models must be pre-trained and configured for test mode.
- The test suite assumes a specific directory structure for the `services` module.
- Ensure the six additional services are compatible with the NLP models and properly handle the input/output formats.
- Test failures may indicate issues with model predictions or misconfigured services.

