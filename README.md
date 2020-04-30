# TeXoo - Model Wrapper for Python (teXooPy)

The basic idea behind this project is to have a central Python module that tackles the handling of [TeXoo](https://github.com/DATEXIS/TeXoo) style JSON data.
The development will happen iteratively, so feel free to contribute and add the features you need.
The goal is not to have a holistic representation of the full TeXoo model but rather to avoid developing model parsing twice.

## State of Implementation

| Class                 | Attributes         | .from_json()       | .to_json() |
| --------------------- | ------------------ | ------------------ | ---------- |
| Dataset               | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Document              | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Span                  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Sentence              | :broken_heart:     | :broken_heart:     | :broken_heart:     |
| Token                 | :broken_heart:     | :broken_heart:     | :broken_heart:     |
| Annotation            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| MentionAnnotation     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| NamedEntityAnnotation | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| SectionAnnotation     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |


:broken_heart: = Implemented but untested

## Executing Unit Tests

`python3 -m unittest texoopy/tests/tests.py`