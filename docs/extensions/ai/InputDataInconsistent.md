---
search:
  boost: 10.0
---

# Class: InputDataInconsistent 


_Concept representing input data being inconsistent_



<div data-search-exclude markdown="1">



URI: [ai:InputDataInconsistent](https://w3id.org/lmodel/dpv/ai/InputDataInconsistent)





```mermaid
 classDiagram
    class InputDataInconsistent
    click InputDataInconsistent href "../InputDataInconsistent/"
      RiskConcept <|-- InputDataInconsistent
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataInconsistent
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataInconsistent** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataInconsistent](https://w3id.org/lmodel/dpv/ai/InputDataInconsistent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Inconsistent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataInconsistent |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataInconsistent |
| native | ai:InputDataInconsistent |
| exact | dpv_ai:InputDataInconsistent, dpv_ai_owl:InputDataInconsistent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being inconsistent
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Inconsistent
exact_mappings:
- dpv_ai:InputDataInconsistent
- dpv_ai_owl:InputDataInconsistent
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataInconsistent

```
</details>

### Induced

<details>
```yaml
name: InputDataInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being inconsistent
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Inconsistent
exact_mappings:
- dpv_ai:InputDataInconsistent
- dpv_ai_owl:InputDataInconsistent
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataInconsistent

```
</details></div>