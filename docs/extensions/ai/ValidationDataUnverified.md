---
search:
  boost: 10.0
---

# Class: ValidationDataUnverified 


_Concept representing validation data being unverified_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataUnverified](https://w3id.org/lmodel/dpv/ai/ValidationDataUnverified)





```mermaid
 classDiagram
    class ValidationDataUnverified
    click ValidationDataUnverified href "../ValidationDataUnverified/"
      RiskConcept <|-- ValidationDataUnverified
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataUnverified
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataUnverified** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataUnverified](https://w3id.org/lmodel/dpv/ai/ValidationDataUnverified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Unverified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataUnverified |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataUnverified |
| native | ai:ValidationDataUnverified |
| exact | dpv_ai:ValidationDataUnverified, dpv_ai_owl:ValidationDataUnverified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being unverified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Unverified
exact_mappings:
- dpv_ai:ValidationDataUnverified
- dpv_ai_owl:ValidationDataUnverified
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataUnverified

```
</details>

### Induced

<details>
```yaml
name: ValidationDataUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being unverified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Unverified
exact_mappings:
- dpv_ai:ValidationDataUnverified
- dpv_ai_owl:ValidationDataUnverified
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataUnverified

```
</details></div>