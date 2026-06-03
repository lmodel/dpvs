---
search:
  boost: 10.0
---

# Class: ValidationDataUnrepresentative 


_Concept representing validation data being unrepresentative_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataUnrepresentative](https://w3id.org/lmodel/dpv/ai/ValidationDataUnrepresentative)





```mermaid
 classDiagram
    class ValidationDataUnrepresentative
    click ValidationDataUnrepresentative href "../ValidationDataUnrepresentative/"
      RiskConcept <|-- ValidationDataUnrepresentative
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataUnrepresentative
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataUnrepresentative** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataUnrepresentative](https://w3id.org/lmodel/dpv/ai/ValidationDataUnrepresentative) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Unrepresentative




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataUnrepresentative |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataUnrepresentative |
| native | ai:ValidationDataUnrepresentative |
| exact | dpv_ai:ValidationDataUnrepresentative, dpv_ai_owl:ValidationDataUnrepresentative |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataUnrepresentative
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataUnrepresentative
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being unrepresentative
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Unrepresentative
exact_mappings:
- dpv_ai:ValidationDataUnrepresentative
- dpv_ai_owl:ValidationDataUnrepresentative
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataUnrepresentative

```
</details>

### Induced

<details>
```yaml
name: ValidationDataUnrepresentative
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataUnrepresentative
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being unrepresentative
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Unrepresentative
exact_mappings:
- dpv_ai:ValidationDataUnrepresentative
- dpv_ai_owl:ValidationDataUnrepresentative
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataUnrepresentative

```
</details></div>