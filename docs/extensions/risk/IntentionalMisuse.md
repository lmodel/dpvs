---
search:
  boost: 10.0
---

# Class: IntentionalMisuse 


_Concept represent an intentional misuse (of something)_



<div data-search-exclude markdown="1">



URI: [risk:IntentionalMisuse](https://w3id.org/lmodel/dpv/risk/IntentionalMisuse)





```mermaid
 classDiagram
    class IntentionalMisuse
    click IntentionalMisuse href "../IntentionalMisuse/"
      PotentialConsequence <|-- IntentionalMisuse
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- IntentionalMisuse
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- IntentionalMisuse
        click PotentialRiskSource href "../PotentialRiskSource/"
      Misuse <|-- IntentionalMisuse
        click Misuse href "../Misuse/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [UserRisks](UserRisks.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [Misuse](Misuse.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **IntentionalMisuse** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IntentionalMisuse](https://w3id.org/lmodel/dpv/risk/IntentionalMisuse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Intentional Misuse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IntentionalMisuse |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IntentionalMisuse |
| native | risk:IntentionalMisuse |
| exact | dpv_risk:IntentionalMisuse, dpv_risk_owl:IntentionalMisuse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntentionalMisuse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IntentionalMisuse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept represent an intentional misuse (of something)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Intentional Misuse
exact_mappings:
- dpv_risk:IntentionalMisuse
- dpv_risk_owl:IntentionalMisuse
is_a: Misuse
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IntentionalMisuse

```
</details>

### Induced

<details>
```yaml
name: IntentionalMisuse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IntentionalMisuse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept represent an intentional misuse (of something)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Intentional Misuse
exact_mappings:
- dpv_risk:IntentionalMisuse
- dpv_risk_owl:IntentionalMisuse
is_a: Misuse
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IntentionalMisuse

```
</details></div>