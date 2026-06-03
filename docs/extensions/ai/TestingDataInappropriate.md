---
search:
  boost: 10.0
---

# Class: TestingDataInappropriate 


_Concept representing testing data being inappropriate_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataInappropriate](https://w3id.org/lmodel/dpv/ai/TestingDataInappropriate)





```mermaid
 classDiagram
    class TestingDataInappropriate
    click TestingDataInappropriate href "../TestingDataInappropriate/"
      RiskConcept <|-- TestingDataInappropriate
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataInappropriate
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataInappropriate** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataInappropriate](https://w3id.org/lmodel/dpv/ai/TestingDataInappropriate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Inappropriate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataInappropriate |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataInappropriate |
| native | ai:TestingDataInappropriate |
| exact | dpv_ai:TestingDataInappropriate, dpv_ai_owl:TestingDataInappropriate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataInappropriate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataInappropriate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being inappropriate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Inappropriate
exact_mappings:
- dpv_ai:TestingDataInappropriate
- dpv_ai_owl:TestingDataInappropriate
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataInappropriate

```
</details>

### Induced

<details>
```yaml
name: TestingDataInappropriate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataInappropriate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being inappropriate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Inappropriate
exact_mappings:
- dpv_ai:TestingDataInappropriate
- dpv_ai_owl:TestingDataInappropriate
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataInappropriate

```
</details></div>