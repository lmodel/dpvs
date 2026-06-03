---
search:
  boost: 10.0
---

# Class: TestingDataUnstructured 


_Concept representing testing data being unstructured_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataUnstructured](https://w3id.org/lmodel/dpv/ai/TestingDataUnstructured)





```mermaid
 classDiagram
    class TestingDataUnstructured
    click TestingDataUnstructured href "../TestingDataUnstructured/"
      RiskConcept <|-- TestingDataUnstructured
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataUnstructured
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataUnstructured** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataUnstructured](https://w3id.org/lmodel/dpv/ai/TestingDataUnstructured) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Unstructured




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataUnstructured |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataUnstructured |
| native | ai:TestingDataUnstructured |
| exact | dpv_ai:TestingDataUnstructured, dpv_ai_owl:TestingDataUnstructured |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataUnstructured
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataUnstructured
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being unstructured
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Unstructured
exact_mappings:
- dpv_ai:TestingDataUnstructured
- dpv_ai_owl:TestingDataUnstructured
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataUnstructured

```
</details>

### Induced

<details>
```yaml
name: TestingDataUnstructured
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataUnstructured
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being unstructured
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Unstructured
exact_mappings:
- dpv_ai:TestingDataUnstructured
- dpv_ai_owl:TestingDataUnstructured
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataUnstructured

```
</details></div>