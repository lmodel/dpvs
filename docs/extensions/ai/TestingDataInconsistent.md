---
search:
  boost: 10.0
---

# Class: TestingDataInconsistent 


_Concept representing testing data being inconsistent_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataInconsistent](https://w3id.org/lmodel/dpv/ai/TestingDataInconsistent)





```mermaid
 classDiagram
    class TestingDataInconsistent
    click TestingDataInconsistent href "../TestingDataInconsistent/"
      RiskConcept <|-- TestingDataInconsistent
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataInconsistent
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataInconsistent** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataInconsistent](https://w3id.org/lmodel/dpv/ai/TestingDataInconsistent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Inconsistent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataInconsistent |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataInconsistent |
| native | ai:TestingDataInconsistent |
| exact | dpv_ai:TestingDataInconsistent, dpv_ai_owl:TestingDataInconsistent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being inconsistent
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Inconsistent
exact_mappings:
- dpv_ai:TestingDataInconsistent
- dpv_ai_owl:TestingDataInconsistent
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataInconsistent

```
</details>

### Induced

<details>
```yaml
name: TestingDataInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being inconsistent
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Inconsistent
exact_mappings:
- dpv_ai:TestingDataInconsistent
- dpv_ai_owl:TestingDataInconsistent
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataInconsistent

```
</details></div>