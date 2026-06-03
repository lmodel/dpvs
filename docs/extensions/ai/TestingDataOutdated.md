---
search:
  boost: 10.0
---

# Class: TestingDataOutdated 


_Concept representing testing data being outdated_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataOutdated](https://w3id.org/lmodel/dpv/ai/TestingDataOutdated)





```mermaid
 classDiagram
    class TestingDataOutdated
    click TestingDataOutdated href "../TestingDataOutdated/"
      RiskConcept <|-- TestingDataOutdated
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataOutdated
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataOutdated** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataOutdated](https://w3id.org/lmodel/dpv/ai/TestingDataOutdated) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Outdated




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataOutdated |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataOutdated |
| native | ai:TestingDataOutdated |
| exact | dpv_ai:TestingDataOutdated, dpv_ai_owl:TestingDataOutdated |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataOutdated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataOutdated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being outdated
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Outdated
exact_mappings:
- dpv_ai:TestingDataOutdated
- dpv_ai_owl:TestingDataOutdated
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataOutdated

```
</details>

### Induced

<details>
```yaml
name: TestingDataOutdated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataOutdated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being outdated
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Outdated
exact_mappings:
- dpv_ai:TestingDataOutdated
- dpv_ai_owl:TestingDataOutdated
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataOutdated

```
</details></div>