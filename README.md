# Template Vars Docs

This folder contains a minimal template example for SPAI Hub with `string` and `numeric` inputs.

## Mongo Template Example

Use `template_document_example.json` as a base document for `db.templates`.

## Supported Variable Types

### Text (`string` or `text`)

Supported options:

- `name` (`string`, required)
- `type` (`"string"` or `"text"`, required)
- `placeholder` (`string`, optional)
- `minLength` (`integer > 0`, optional)
- `maxLength` (`integer > 0`, optional)
- `default` (`string`, optional)

Behavior:

- Empty value is stored as `null`.
- `minLength`/`maxLength` are enforced by native input attributes.
- No trimming is applied in the input component.

### Numeric (`numeric` or `number`)

Supported options:

- `name` (`string`, required)
- `type` (`"numeric"` or `"number"`, required)
- `placeholder` (`string`, optional)
- `min` (`number`, optional)
- `max` (`number`, optional)
- `step` (`number > 0`, optional)
- `default` (`number`, optional)

Behavior:

- Empty value is stored as `null`.
- Invalid numeric values are stored as `null`.
- `min`/`max` and `step` are validated in the component.
- Comma decimals are accepted (`12,5` -> `12.5`).

## Mongo Edge Cases Covered

- If `template.variables` is missing or not an array, no variable inputs are rendered.
- If a variable is missing `name` or `type`, it is ignored.
- Duplicate variable names are ignored after the first valid one.
- If `min > max` (or `minLength > maxLength`), values are normalized automatically.

## Quick Local Test

1. Insert/update your template in Mongo using `template_document_example.json`.
2. Run backend and UI locally.
3. Open `/hub/<template-id>`.
4. Verify:
   - `MESSAGE` renders as text input.
   - `MAX_ITEMS` renders as numeric input.
