---
search:
  boost: 10.0
---

# Class: ValidationDataMisinterpretation 


_Concept representing validation data being misinterpreted_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataMisinterpretation](https://w3id.org/lmodel/dpv/ai/ValidationDataMisinterpretation)





```mermaid
 classDiagram
    class ValidationDataMisinterpretation
    click ValidationDataMisinterpretation href "../ValidationDataMisinterpretation/"
      RiskConcept <|-- ValidationDataMisinterpretation
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataMisinterpretation
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataMisinterpretation** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataMisinterpretation](https://w3id.org/lmodel/dpv/ai/ValidationDataMisinterpretation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Misinterpretation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataMisinterpretation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataMisinterpretation |
| native | ai:ValidationDataMisinterpretation |
| exact | dpv_ai:ValidationDataMisinterpretation, dpv_ai_owl:ValidationDataMisinterpretation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataMisinterpretation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataMisinterpretation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being misinterpreted
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Misinterpretation
exact_mappings:
- dpv_ai:ValidationDataMisinterpretation
- dpv_ai_owl:ValidationDataMisinterpretation
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataMisinterpretation

```
</details>

### Induced

<details>
```yaml
name: ValidationDataMisinterpretation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataMisinterpretation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being misinterpreted
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Misinterpretation
exact_mappings:
- dpv_ai:ValidationDataMisinterpretation
- dpv_ai_owl:ValidationDataMisinterpretation
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataMisinterpretation

```
</details></div>