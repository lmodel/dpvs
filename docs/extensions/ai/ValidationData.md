---
search:
  boost: 10.0
---

# Class: ValidationData 


_Data involved in the validation of an AI system or model_



<div data-search-exclude markdown="1">



URI: [ai:ValidationData](https://w3id.org/lmodel/dpv/ai/ValidationData)





```mermaid
 classDiagram
    class ValidationData
    click ValidationData href "../ValidationData/"
      DpvData <|-- ValidationData
        click DpvData href "../DpvData/"
      
      
```





## Inheritance
* [DpvData](DpvData.md)
    * **ValidationData**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationData](https://w3id.org/lmodel/dpv/ai/ValidationData) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationData |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationData |
| native | ai:ValidationData |
| exact | dpv_ai:ValidationData, dpv_ai_owl:ValidationData |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Data involved in the validation of an AI system or model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data
exact_mappings:
- dpv_ai:ValidationData
- dpv_ai_owl:ValidationData
is_a: DpvData
class_uri: ai:ValidationData

```
</details>

### Induced

<details>
```yaml
name: ValidationData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Data involved in the validation of an AI system or model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data
exact_mappings:
- dpv_ai:ValidationData
- dpv_ai_owl:ValidationData
is_a: DpvData
class_uri: ai:ValidationData

```
</details></div>