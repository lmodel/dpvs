---
search:
  boost: 10.0
---

# Class: InputDataUnverified 


_Concept representing input data being unverified_



<div data-search-exclude markdown="1">



URI: [ai:InputDataUnverified](https://w3id.org/lmodel/dpv/ai/InputDataUnverified)





```mermaid
 classDiagram
    class InputDataUnverified
    click InputDataUnverified href "../InputDataUnverified/"
      RiskConcept <|-- InputDataUnverified
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataUnverified
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataUnverified** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataUnverified](https://w3id.org/lmodel/dpv/ai/InputDataUnverified) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Unverified




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataUnverified |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataUnverified |
| native | ai:InputDataUnverified |
| exact | dpv_ai:InputDataUnverified, dpv_ai_owl:InputDataUnverified |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being unverified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Unverified
exact_mappings:
- dpv_ai:InputDataUnverified
- dpv_ai_owl:InputDataUnverified
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataUnverified

```
</details>

### Induced

<details>
```yaml
name: InputDataUnverified
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataUnverified
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being unverified
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Unverified
exact_mappings:
- dpv_ai:InputDataUnverified
- dpv_ai_owl:InputDataUnverified
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataUnverified

```
</details></div>