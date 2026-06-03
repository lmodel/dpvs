---
search:
  boost: 10.0
---

# Class: ValidationDataInaccurate 


_Concept representing validation data being inaccurate_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataInaccurate](https://w3id.org/lmodel/dpv/ai/ValidationDataInaccurate)





```mermaid
 classDiagram
    class ValidationDataInaccurate
    click ValidationDataInaccurate href "../ValidationDataInaccurate/"
      RiskConcept <|-- ValidationDataInaccurate
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataInaccurate
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataInaccurate** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataInaccurate](https://w3id.org/lmodel/dpv/ai/ValidationDataInaccurate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Inaccurate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataInaccurate |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataInaccurate |
| native | ai:ValidationDataInaccurate |
| exact | dpv_ai:ValidationDataInaccurate, dpv_ai_owl:ValidationDataInaccurate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataInaccurate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataInaccurate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being inaccurate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Inaccurate
exact_mappings:
- dpv_ai:ValidationDataInaccurate
- dpv_ai_owl:ValidationDataInaccurate
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataInaccurate

```
</details>

### Induced

<details>
```yaml
name: ValidationDataInaccurate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataInaccurate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being inaccurate
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Inaccurate
exact_mappings:
- dpv_ai:ValidationDataInaccurate
- dpv_ai_owl:ValidationDataInaccurate
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataInaccurate

```
</details></div>