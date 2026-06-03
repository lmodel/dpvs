---
search:
  boost: 10.0
---

# Class: InputDataOutdated 


_Concept representing input data being outdated_



<div data-search-exclude markdown="1">



URI: [ai:InputDataOutdated](https://w3id.org/lmodel/dpv/ai/InputDataOutdated)





```mermaid
 classDiagram
    class InputDataOutdated
    click InputDataOutdated href "../InputDataOutdated/"
      RiskConcept <|-- InputDataOutdated
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataOutdated
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataOutdated** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataOutdated](https://w3id.org/lmodel/dpv/ai/InputDataOutdated) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Outdated




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataOutdated |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataOutdated |
| native | ai:InputDataOutdated |
| exact | dpv_ai:InputDataOutdated, dpv_ai_owl:InputDataOutdated |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataOutdated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataOutdated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being outdated
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Outdated
exact_mappings:
- dpv_ai:InputDataOutdated
- dpv_ai_owl:InputDataOutdated
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataOutdated

```
</details>

### Induced

<details>
```yaml
name: InputDataOutdated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataOutdated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being outdated
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Outdated
exact_mappings:
- dpv_ai:InputDataOutdated
- dpv_ai_owl:InputDataOutdated
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataOutdated

```
</details></div>