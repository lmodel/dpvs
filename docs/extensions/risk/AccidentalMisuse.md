---
search:
  boost: 10.0
---

# Class: AccidentalMisuse 


_Concept representing accidental misuse (of something)_



<div data-search-exclude markdown="1">



URI: [risk:AccidentalMisuse](https://w3id.org/lmodel/dpv/risk/AccidentalMisuse)





```mermaid
 classDiagram
    class AccidentalMisuse
    click AccidentalMisuse href "../AccidentalMisuse/"
      PotentialConsequence <|-- AccidentalMisuse
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- AccidentalMisuse
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- AccidentalMisuse
        click PotentialRiskSource href "../PotentialRiskSource/"
      Misuse <|-- AccidentalMisuse
        click Misuse href "../Misuse/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [UserRisks](UserRisks.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [Misuse](Misuse.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **AccidentalMisuse** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AccidentalMisuse](https://w3id.org/lmodel/dpv/risk/AccidentalMisuse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Accidental Misuse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AccidentalMisuse |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AccidentalMisuse |
| native | risk:AccidentalMisuse |
| exact | dpv_risk:AccidentalMisuse, dpv_risk_owl:AccidentalMisuse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AccidentalMisuse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccidentalMisuse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing accidental misuse (of something)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accidental Misuse
exact_mappings:
- dpv_risk:AccidentalMisuse
- dpv_risk_owl:AccidentalMisuse
is_a: Misuse
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:AccidentalMisuse

```
</details>

### Induced

<details>
```yaml
name: AccidentalMisuse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccidentalMisuse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing accidental misuse (of something)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accidental Misuse
exact_mappings:
- dpv_risk:AccidentalMisuse
- dpv_risk_owl:AccidentalMisuse
is_a: Misuse
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:AccidentalMisuse

```
</details></div>