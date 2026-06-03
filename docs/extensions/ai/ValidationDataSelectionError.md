---
search:
  boost: 10.0
---

# Class: ValidationDataSelectionError 


_Concept representing an error in validation data selection_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataSelectionError](https://w3id.org/lmodel/dpv/ai/ValidationDataSelectionError)





```mermaid
 classDiagram
    class ValidationDataSelectionError
    click ValidationDataSelectionError href "../ValidationDataSelectionError/"
      RiskConcept <|-- ValidationDataSelectionError
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataSelectionError
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataSelectionError** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataSelectionError](https://w3id.org/lmodel/dpv/ai/ValidationDataSelectionError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Selection Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataSelectionError |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataSelectionError |
| native | ai:ValidationDataSelectionError |
| exact | dpv_ai:ValidationDataSelectionError, dpv_ai_owl:ValidationDataSelectionError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataSelectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataSelectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing an error in validation data selection
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Selection Error
exact_mappings:
- dpv_ai:ValidationDataSelectionError
- dpv_ai_owl:ValidationDataSelectionError
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataSelectionError

```
</details>

### Induced

<details>
```yaml
name: ValidationDataSelectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataSelectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing an error in validation data selection
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Selection Error
exact_mappings:
- dpv_ai:ValidationDataSelectionError
- dpv_ai_owl:ValidationDataSelectionError
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataSelectionError

```
</details></div>