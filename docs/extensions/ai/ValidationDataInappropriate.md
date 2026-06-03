---
search:
  boost: 10.0
---

# Class: ValidationDataInappropriate 


_Concept representing validation data being inappropriate_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataInappropriate](https://w3id.org/lmodel/dpv/ai/ValidationDataInappropriate)





```mermaid
 classDiagram
    class ValidationDataInappropriate
    click ValidationDataInappropriate href "../ValidationDataInappropriate/"
      RiskConcept <|-- ValidationDataInappropriate
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataInappropriate
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataInappropriate** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataInappropriate](https://w3id.org/lmodel/dpv/ai/ValidationDataInappropriate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Inappropriate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataInappropriate |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataInappropriate |
| native | ai:ValidationDataInappropriate |
| exact | dpv_ai:ValidationDataInappropriate, dpv_ai_owl:ValidationDataInappropriate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataInappropriate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataInappropriate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being inappropriate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Inappropriate
exact_mappings:
- dpv_ai:ValidationDataInappropriate
- dpv_ai_owl:ValidationDataInappropriate
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataInappropriate

```
</details>

### Induced

<details>
```yaml
name: ValidationDataInappropriate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataInappropriate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being inappropriate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Inappropriate
exact_mappings:
- dpv_ai:ValidationDataInappropriate
- dpv_ai_owl:ValidationDataInappropriate
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataInappropriate

```
</details></div>