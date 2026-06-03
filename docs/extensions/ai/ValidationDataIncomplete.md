---
search:
  boost: 10.0
---

# Class: ValidationDataIncomplete 


_Concept representing validation data being incomplete_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataIncomplete](https://w3id.org/lmodel/dpv/ai/ValidationDataIncomplete)





```mermaid
 classDiagram
    class ValidationDataIncomplete
    click ValidationDataIncomplete href "../ValidationDataIncomplete/"
      RiskConcept <|-- ValidationDataIncomplete
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataIncomplete
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataIncomplete** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataIncomplete](https://w3id.org/lmodel/dpv/ai/ValidationDataIncomplete) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Incomplete




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataIncomplete |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataIncomplete |
| native | ai:ValidationDataIncomplete |
| exact | dpv_ai:ValidationDataIncomplete, dpv_ai_owl:ValidationDataIncomplete |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataIncomplete
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataIncomplete
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being incomplete
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Incomplete
exact_mappings:
- dpv_ai:ValidationDataIncomplete
- dpv_ai_owl:ValidationDataIncomplete
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataIncomplete

```
</details>

### Induced

<details>
```yaml
name: ValidationDataIncomplete
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataIncomplete
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being incomplete
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Incomplete
exact_mappings:
- dpv_ai:ValidationDataIncomplete
- dpv_ai_owl:ValidationDataIncomplete
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataIncomplete

```
</details></div>