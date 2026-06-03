---
search:
  boost: 10.0
---

# Class: AdversarialAttack 


_Inputs designed to cause the model to make a mistake_



<div data-search-exclude markdown="1">



URI: [ai:AdversarialAttack](https://w3id.org/lmodel/dpv/ai/AdversarialAttack)





```mermaid
 classDiagram
    class AdversarialAttack
    click AdversarialAttack href "../AdversarialAttack/"
      RiskConcept <|-- AdversarialAttack
        click RiskConcept href "../RiskConcept/"
      SecurityAttack <|-- AdversarialAttack
        click SecurityAttack href "../SecurityAttack/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [SecurityAttack](SecurityAttack.md)
        * **AdversarialAttack** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:AdversarialAttack](https://w3id.org/lmodel/dpv/ai/AdversarialAttack) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Adversarial Attack




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#AdversarialAttack |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:AdversarialAttack |
| native | ai:AdversarialAttack |
| exact | dpv_ai:AdversarialAttack, dpv_ai_owl:AdversarialAttack |
| close | iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AdversarialAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AdversarialAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Inputs designed to cause the model to make a mistake
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Adversarial Attack
exact_mappings:
- dpv_ai:AdversarialAttack
- dpv_ai_owl:AdversarialAttack
close_mappings:
- iso42001:AIIncident
is_a: SecurityAttack
mixins:
- RiskConcept
class_uri: ai:AdversarialAttack

```
</details>

### Induced

<details>
```yaml
name: AdversarialAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AdversarialAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Inputs designed to cause the model to make a mistake
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Adversarial Attack
exact_mappings:
- dpv_ai:AdversarialAttack
- dpv_ai_owl:AdversarialAttack
close_mappings:
- iso42001:AIIncident
is_a: SecurityAttack
mixins:
- RiskConcept
class_uri: ai:AdversarialAttack

```
</details></div>