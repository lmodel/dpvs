---
search:
  boost: 10.0
---

# Class: InputDataUnstructured 


_Concept representing input data being unstructured_



<div data-search-exclude markdown="1">



URI: [ai:InputDataUnstructured](https://w3id.org/lmodel/dpv/ai/InputDataUnstructured)





```mermaid
 classDiagram
    class InputDataUnstructured
    click InputDataUnstructured href "../InputDataUnstructured/"
      RiskConcept <|-- InputDataUnstructured
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataUnstructured
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataUnstructured** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataUnstructured](https://w3id.org/lmodel/dpv/ai/InputDataUnstructured) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Unstructured




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataUnstructured |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataUnstructured |
| native | ai:InputDataUnstructured |
| exact | dpv_ai:InputDataUnstructured, dpv_ai_owl:InputDataUnstructured |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataUnstructured
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataUnstructured
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being unstructured
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Unstructured
exact_mappings:
- dpv_ai:InputDataUnstructured
- dpv_ai_owl:InputDataUnstructured
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataUnstructured

```
</details>

### Induced

<details>
```yaml
name: InputDataUnstructured
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataUnstructured
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being unstructured
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Unstructured
exact_mappings:
- dpv_ai:InputDataUnstructured
- dpv_ai_owl:InputDataUnstructured
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataUnstructured

```
</details></div>