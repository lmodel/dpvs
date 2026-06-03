---
search:
  boost: 10.0
---

# Class: LegallyRelevantConsequence 


_A consequence that is legally relevant i.e. actionable under law_



<div data-search-exclude markdown="1">



URI: [risk:LegallyRelevantConsequence](https://w3id.org/lmodel/dpv/risk/LegallyRelevantConsequence)





```mermaid
 classDiagram
    class LegallyRelevantConsequence
    click LegallyRelevantConsequence href "../LegallyRelevantConsequence/"
      PotentialConsequence <|-- LegallyRelevantConsequence
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- LegallyRelevantConsequence
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- LegallyRelevantConsequence
        click PotentialRisk href "../PotentialRisk/"
      LegalRiskConcept <|-- LegallyRelevantConsequence
        click LegalRiskConcept href "../LegalRiskConcept/"
      

      LegallyRelevantConsequence <|-- Damage
        click Damage href "../Damage/"
      LegallyRelevantConsequence <|-- Detriment
        click Detriment href "../Detriment/"
      LegallyRelevantConsequence <|-- MaterialDamage
        click MaterialDamage href "../MaterialDamage/"
      LegallyRelevantConsequence <|-- NonMaterialDamage
        click NonMaterialDamage href "../NonMaterialDamage/"
      

      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **LegallyRelevantConsequence** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Damage](Damage.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Detriment](Detriment.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [MaterialDamage](MaterialDamage.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [NonMaterialDamage](NonMaterialDamage.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LegallyRelevantConsequence](https://w3id.org/lmodel/dpv/risk/LegallyRelevantConsequence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Legally Relevant Consequence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LegallyRelevantConsequence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LegallyRelevantConsequence |
| native | risk:LegallyRelevantConsequence |
| exact | dpv_risk:LegallyRelevantConsequence, dpv_risk_owl:LegallyRelevantConsequence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegallyRelevantConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LegallyRelevantConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: A consequence that is legally relevant i.e. actionable under law
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Legally Relevant Consequence
exact_mappings:
- dpv_risk:LegallyRelevantConsequence
- dpv_risk_owl:LegallyRelevantConsequence
is_a: LegalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:LegallyRelevantConsequence

```
</details>

### Induced

<details>
```yaml
name: LegallyRelevantConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LegallyRelevantConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: A consequence that is legally relevant i.e. actionable under law
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Legally Relevant Consequence
exact_mappings:
- dpv_risk:LegallyRelevantConsequence
- dpv_risk_owl:LegallyRelevantConsequence
is_a: LegalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:LegallyRelevantConsequence

```
</details></div>