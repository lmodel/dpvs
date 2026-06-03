---
search:
  boost: 10.0
---

# Class: ValidationDataInconsistent 


_Concept representing validation data being inconsistent_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataInconsistent](https://w3id.org/lmodel/dpv/ai/ValidationDataInconsistent)





```mermaid
 classDiagram
    class ValidationDataInconsistent
    click ValidationDataInconsistent href "../ValidationDataInconsistent/"
      RiskConcept <|-- ValidationDataInconsistent
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataInconsistent
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataInconsistent** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataInconsistent](https://w3id.org/lmodel/dpv/ai/ValidationDataInconsistent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Inconsistent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataInconsistent |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataInconsistent |
| native | ai:ValidationDataInconsistent |
| exact | dpv_ai:ValidationDataInconsistent, dpv_ai_owl:ValidationDataInconsistent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being inconsistent
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Inconsistent
exact_mappings:
- dpv_ai:ValidationDataInconsistent
- dpv_ai_owl:ValidationDataInconsistent
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataInconsistent

```
</details>

### Induced

<details>
```yaml
name: ValidationDataInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being inconsistent
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Inconsistent
exact_mappings:
- dpv_ai:ValidationDataInconsistent
- dpv_ai_owl:ValidationDataInconsistent
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataInconsistent

```
</details></div>