---
search:
  boost: 10.0
---

# Class: InputDataUnrepresentative 


_Concept representing input data being unrepresentative_



<div data-search-exclude markdown="1">



URI: [ai:InputDataUnrepresentative](https://w3id.org/lmodel/dpv/ai/InputDataUnrepresentative)





```mermaid
 classDiagram
    class InputDataUnrepresentative
    click InputDataUnrepresentative href "../InputDataUnrepresentative/"
      RiskConcept <|-- InputDataUnrepresentative
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataUnrepresentative
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataUnrepresentative** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataUnrepresentative](https://w3id.org/lmodel/dpv/ai/InputDataUnrepresentative) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Unrepresentative




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataUnrepresentative |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataUnrepresentative |
| native | ai:InputDataUnrepresentative |
| exact | dpv_ai:InputDataUnrepresentative, dpv_ai_owl:InputDataUnrepresentative |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataUnrepresentative
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataUnrepresentative
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being unrepresentative
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Unrepresentative
exact_mappings:
- dpv_ai:InputDataUnrepresentative
- dpv_ai_owl:InputDataUnrepresentative
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataUnrepresentative

```
</details>

### Induced

<details>
```yaml
name: InputDataUnrepresentative
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataUnrepresentative
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being unrepresentative
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Unrepresentative
exact_mappings:
- dpv_ai:InputDataUnrepresentative
- dpv_ai_owl:InputDataUnrepresentative
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataUnrepresentative

```
</details></div>