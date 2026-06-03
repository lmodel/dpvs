---
search:
  boost: 10.0
---

# Class: ValidationDataMisclassified 


_Concept representing validation data being misclassified_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataMisclassified](https://w3id.org/lmodel/dpv/ai/ValidationDataMisclassified)





```mermaid
 classDiagram
    class ValidationDataMisclassified
    click ValidationDataMisclassified href "../ValidationDataMisclassified/"
      RiskConcept <|-- ValidationDataMisclassified
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataMisclassified
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataMisclassified** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataMisclassified](https://w3id.org/lmodel/dpv/ai/ValidationDataMisclassified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Misclassified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataMisclassified |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataMisclassified |
| native | ai:ValidationDataMisclassified |
| exact | dpv_ai:ValidationDataMisclassified, dpv_ai_owl:ValidationDataMisclassified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataMisclassified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataMisclassified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being misclassified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Misclassified
exact_mappings:
- dpv_ai:ValidationDataMisclassified
- dpv_ai_owl:ValidationDataMisclassified
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataMisclassified

```
</details>

### Induced

<details>
```yaml
name: ValidationDataMisclassified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataMisclassified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being misclassified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Misclassified
exact_mappings:
- dpv_ai:ValidationDataMisclassified
- dpv_ai_owl:ValidationDataMisclassified
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataMisclassified

```
</details></div>