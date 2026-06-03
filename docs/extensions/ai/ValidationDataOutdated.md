---
search:
  boost: 10.0
---

# Class: ValidationDataOutdated 


_Concept representing validation data being outdated_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataOutdated](https://w3id.org/lmodel/dpv/ai/ValidationDataOutdated)





```mermaid
 classDiagram
    class ValidationDataOutdated
    click ValidationDataOutdated href "../ValidationDataOutdated/"
      RiskConcept <|-- ValidationDataOutdated
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataOutdated
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataOutdated** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataOutdated](https://w3id.org/lmodel/dpv/ai/ValidationDataOutdated) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Outdated




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataOutdated |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataOutdated |
| native | ai:ValidationDataOutdated |
| exact | dpv_ai:ValidationDataOutdated, dpv_ai_owl:ValidationDataOutdated |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataOutdated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataOutdated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being outdated
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Outdated
exact_mappings:
- dpv_ai:ValidationDataOutdated
- dpv_ai_owl:ValidationDataOutdated
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataOutdated

```
</details>

### Induced

<details>
```yaml
name: ValidationDataOutdated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataOutdated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being outdated
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Outdated
exact_mappings:
- dpv_ai:ValidationDataOutdated
- dpv_ai_owl:ValidationDataOutdated
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataOutdated

```
</details></div>