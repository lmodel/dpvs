---
search:
  boost: 10.0
---

# Class: ValidationDataUnstructured 


_Concept representing validation data being unstructured_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataUnstructured](https://w3id.org/lmodel/dpv/ai/ValidationDataUnstructured)





```mermaid
 classDiagram
    class ValidationDataUnstructured
    click ValidationDataUnstructured href "../ValidationDataUnstructured/"
      RiskConcept <|-- ValidationDataUnstructured
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataUnstructured
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataUnstructured** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataUnstructured](https://w3id.org/lmodel/dpv/ai/ValidationDataUnstructured) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Unstructured




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataUnstructured |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataUnstructured |
| native | ai:ValidationDataUnstructured |
| exact | dpv_ai:ValidationDataUnstructured, dpv_ai_owl:ValidationDataUnstructured |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataUnstructured
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataUnstructured
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being unstructured
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Unstructured
exact_mappings:
- dpv_ai:ValidationDataUnstructured
- dpv_ai_owl:ValidationDataUnstructured
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataUnstructured

```
</details>

### Induced

<details>
```yaml
name: ValidationDataUnstructured
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataUnstructured
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being unstructured
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Unstructured
exact_mappings:
- dpv_ai:ValidationDataUnstructured
- dpv_ai_owl:ValidationDataUnstructured
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataUnstructured

```
</details></div>