---
search:
  boost: 10.0
---

# Class: TestingDataInaccurate 


_Concept representing testing data being inaccurate_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataInaccurate](https://w3id.org/lmodel/dpv/ai/TestingDataInaccurate)





```mermaid
 classDiagram
    class TestingDataInaccurate
    click TestingDataInaccurate href "../TestingDataInaccurate/"
      RiskConcept <|-- TestingDataInaccurate
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataInaccurate
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataInaccurate** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataInaccurate](https://w3id.org/lmodel/dpv/ai/TestingDataInaccurate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Inaccurate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataInaccurate |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataInaccurate |
| native | ai:TestingDataInaccurate |
| exact | dpv_ai:TestingDataInaccurate, dpv_ai_owl:TestingDataInaccurate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataInaccurate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataInaccurate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being inaccurate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Inaccurate
exact_mappings:
- dpv_ai:TestingDataInaccurate
- dpv_ai_owl:TestingDataInaccurate
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataInaccurate

```
</details>

### Induced

<details>
```yaml
name: TestingDataInaccurate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataInaccurate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being inaccurate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Inaccurate
exact_mappings:
- dpv_ai:TestingDataInaccurate
- dpv_ai_owl:TestingDataInaccurate
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataInaccurate

```
</details></div>