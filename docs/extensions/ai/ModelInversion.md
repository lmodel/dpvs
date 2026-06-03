---
search:
  boost: 10.0
---

# Class: ModelInversion 


_A type of attack to AI models, in which the access to a model is abused_

_to infer information about the training data_



<div data-search-exclude markdown="1">



URI: [ai:ModelInversion](https://w3id.org/lmodel/dpv/ai/ModelInversion)





```mermaid
 classDiagram
    class ModelInversion
    click ModelInversion href "../ModelInversion/"
      RiskConcept <|-- ModelInversion
        click RiskConcept href "../RiskConcept/"
      SecurityAttack <|-- ModelInversion
        click SecurityAttack href "../SecurityAttack/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [SecurityAttack](SecurityAttack.md)
        * **ModelInversion** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ModelInversion](https://w3id.org/lmodel/dpv/ai/ModelInversion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Model Inversion


## Comments

* (HLEG Assessment List for Trustworthy Artificial Intelligence
(ALTAI),https://digital-strategy.ec.europa.eu/en/library/assessment-list-trustworthy-artificial-intelligence-altai-self-assessment)



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ModelInversion |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ModelInversion |
| native | ai:ModelInversion |
| exact | dpv_ai:ModelInversion, dpv_ai_owl:ModelInversion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModelInversion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ModelInversion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'A type of attack to AI models, in which the access to a model is abused

  to infer information about the training data'
comments:
- '(HLEG Assessment List for Trustworthy Artificial Intelligence

  (ALTAI),https://digital-strategy.ec.europa.eu/en/library/assessment-list-trustworthy-artificial-intelligence-altai-self-assessment)'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Model Inversion
exact_mappings:
- dpv_ai:ModelInversion
- dpv_ai_owl:ModelInversion
is_a: SecurityAttack
mixins:
- RiskConcept
class_uri: ai:ModelInversion

```
</details>

### Induced

<details>
```yaml
name: ModelInversion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ModelInversion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'A type of attack to AI models, in which the access to a model is abused

  to infer information about the training data'
comments:
- '(HLEG Assessment List for Trustworthy Artificial Intelligence

  (ALTAI),https://digital-strategy.ec.europa.eu/en/library/assessment-list-trustworthy-artificial-intelligence-altai-self-assessment)'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Model Inversion
exact_mappings:
- dpv_ai:ModelInversion
- dpv_ai_owl:ModelInversion
is_a: SecurityAttack
mixins:
- RiskConcept
class_uri: ai:ModelInversion

```
</details></div>