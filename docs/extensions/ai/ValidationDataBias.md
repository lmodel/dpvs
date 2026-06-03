---
search:
  boost: 10.0
---

# Class: ValidationDataBias 


_Concept representing validation data containing or potentially_

_containing bias_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataBias](https://w3id.org/lmodel/dpv/ai/ValidationDataBias)





```mermaid
 classDiagram
    class ValidationDataBias
    click ValidationDataBias href "../ValidationDataBias/"
      RiskConcept <|-- ValidationDataBias
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataBias
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataBias** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataBias](https://w3id.org/lmodel/dpv/ai/ValidationDataBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataBias |
| native | ai:ValidationDataBias |
| exact | dpv_ai:ValidationDataBias, dpv_ai_owl:ValidationDataBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataBias
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Concept representing validation data containing or potentially

  containing bias'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Bias
exact_mappings:
- dpv_ai:ValidationDataBias
- dpv_ai_owl:ValidationDataBias
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataBias

```
</details>

### Induced

<details>
```yaml
name: ValidationDataBias
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Concept representing validation data containing or potentially

  containing bias'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Bias
exact_mappings:
- dpv_ai:ValidationDataBias
- dpv_ai_owl:ValidationDataBias
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataBias

```
</details></div>