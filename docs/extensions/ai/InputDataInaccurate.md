---
search:
  boost: 10.0
---

# Class: InputDataInaccurate 


_Concept representing input data being inaccurate_



<div data-search-exclude markdown="1">



URI: [ai:InputDataInaccurate](https://w3id.org/lmodel/dpv/ai/InputDataInaccurate)





```mermaid
 classDiagram
    class InputDataInaccurate
    click InputDataInaccurate href "../InputDataInaccurate/"
      RiskConcept <|-- InputDataInaccurate
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataInaccurate
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataInaccurate** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataInaccurate](https://w3id.org/lmodel/dpv/ai/InputDataInaccurate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Inaccurate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataInaccurate |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataInaccurate |
| native | ai:InputDataInaccurate |
| exact | dpv_ai:InputDataInaccurate, dpv_ai_owl:InputDataInaccurate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataInaccurate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataInaccurate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being inaccurate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Inaccurate
exact_mappings:
- dpv_ai:InputDataInaccurate
- dpv_ai_owl:InputDataInaccurate
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataInaccurate

```
</details>

### Induced

<details>
```yaml
name: InputDataInaccurate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataInaccurate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being inaccurate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Inaccurate
exact_mappings:
- dpv_ai:InputDataInaccurate
- dpv_ai_owl:InputDataInaccurate
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataInaccurate

```
</details></div>