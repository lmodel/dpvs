---
search:
  boost: 10.0
---

# Class: DataRisk 


_Risk associated with data used or produced or otherwise involved in the_

_context of AI_



<div data-search-exclude markdown="1">



URI: [ai:DataRisk](https://w3id.org/lmodel/dpv/ai/DataRisk)





```mermaid
 classDiagram
    class DataRisk
    click DataRisk href "../DataRisk/"
      RiskConcept <|-- DataRisk
        click RiskConcept href "../RiskConcept/"
      

      DataRisk <|-- InputDataRisk
        click InputDataRisk href "../InputDataRisk/"
      DataRisk <|-- TestingDataRisk
        click TestingDataRisk href "../TestingDataRisk/"
      DataRisk <|-- ValidationDataRisk
        click ValidationDataRisk href "../ValidationDataRisk/"
      

      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * **DataRisk**
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataRisk](https://w3id.org/lmodel/dpv/ai/DataRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataRisk |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataRisk |
| native | ai:DataRisk |
| exact | dpv_ai:DataRisk, dpv_ai_owl:DataRisk |
| related | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Risk associated with data used or produced or otherwise involved in
  the

  context of AI'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Risk
exact_mappings:
- dpv_ai:DataRisk
- dpv_ai_owl:DataRisk
related_mappings:
- iso42001:AIRisk
is_a: RiskConcept
class_uri: ai:DataRisk

```
</details>

### Induced

<details>
```yaml
name: DataRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Risk associated with data used or produced or otherwise involved in
  the

  context of AI'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Risk
exact_mappings:
- dpv_ai:DataRisk
- dpv_ai_owl:DataRisk
related_mappings:
- iso42001:AIRisk
is_a: RiskConcept
class_uri: ai:DataRisk

```
</details></div>