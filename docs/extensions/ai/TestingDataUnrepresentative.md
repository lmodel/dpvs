---
search:
  boost: 10.0
---

# Class: TestingDataUnrepresentative 


_Concept representing testing data being unrepresentative_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataUnrepresentative](https://w3id.org/lmodel/dpv/ai/TestingDataUnrepresentative)





```mermaid
 classDiagram
    class TestingDataUnrepresentative
    click TestingDataUnrepresentative href "../TestingDataUnrepresentative/"
      RiskConcept <|-- TestingDataUnrepresentative
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataUnrepresentative
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataUnrepresentative** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataUnrepresentative](https://w3id.org/lmodel/dpv/ai/TestingDataUnrepresentative) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Unrepresentative




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataUnrepresentative |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataUnrepresentative |
| native | ai:TestingDataUnrepresentative |
| exact | dpv_ai:TestingDataUnrepresentative, dpv_ai_owl:TestingDataUnrepresentative |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataUnrepresentative
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataUnrepresentative
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being unrepresentative
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Unrepresentative
exact_mappings:
- dpv_ai:TestingDataUnrepresentative
- dpv_ai_owl:TestingDataUnrepresentative
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataUnrepresentative

```
</details>

### Induced

<details>
```yaml
name: TestingDataUnrepresentative
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataUnrepresentative
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being unrepresentative
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Unrepresentative
exact_mappings:
- dpv_ai:TestingDataUnrepresentative
- dpv_ai_owl:TestingDataUnrepresentative
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataUnrepresentative

```
</details></div>