---
search:
  boost: 10.0
---

# Class: InputDataInappropriate 


_Concept representing input data being inappropriate_



<div data-search-exclude markdown="1">



URI: [ai:InputDataInappropriate](https://w3id.org/lmodel/dpv/ai/InputDataInappropriate)





```mermaid
 classDiagram
    class InputDataInappropriate
    click InputDataInappropriate href "../InputDataInappropriate/"
      RiskConcept <|-- InputDataInappropriate
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataInappropriate
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataInappropriate** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataInappropriate](https://w3id.org/lmodel/dpv/ai/InputDataInappropriate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Inappropriate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataInappropriate |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataInappropriate |
| native | ai:InputDataInappropriate |
| exact | dpv_ai:InputDataInappropriate, dpv_ai_owl:InputDataInappropriate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataInappropriate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataInappropriate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being inappropriate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Inappropriate
exact_mappings:
- dpv_ai:InputDataInappropriate
- dpv_ai_owl:InputDataInappropriate
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataInappropriate

```
</details>

### Induced

<details>
```yaml
name: InputDataInappropriate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataInappropriate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being inappropriate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Inappropriate
exact_mappings:
- dpv_ai:InputDataInappropriate
- dpv_ai_owl:InputDataInappropriate
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataInappropriate

```
</details></div>