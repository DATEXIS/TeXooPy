# TeXoo - Model Wrapper for Python (teXooPy)

The basic idea behind this project is to have a central Python module that tackles the handling of TeXoo style JSON data.
The development will happen iteratively, so feel free to contribute and add the features you need.
The goal is not to have a holistic representation of the full TeXoo model but rather to avoid developing model parsing twice.

## State of Implementation

| Class                 | Attributes         | .from_json()       | .to_json() |
| --------------------- | ------------------ | ------------------ | ---------- |
| Dataset               | :heavy_check_mark: | :heavy_check_mark: | :x:        |
| Document              | :heavy_check_mark: | :heavy_check_mark: | :x:        |
| Span                  | :heavy_check_mark: | :x:                | (1)        |
| Sentence              | :x:                | (1)                | (1)        |
| Token                 | :x:                | (1)                | (1)        |
| Annotation            | :heavy_check_mark: | :heavy_check_mark: | :x:        |
| MentionAnnotation     | :heavy_check_mark: | :heavy_check_mark: | :x:        |
| NamedEntityAnnotation | :heavy_check_mark: | :heavy_check_mark: | :x:        |
