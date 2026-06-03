---
search:
  boost: 10.0
---

# Class: EthnicDiscrimination 


_Discrimination against individuals based on their ethnicity or cultural_

_heritage_



<div data-search-exclude markdown="1">



URI: [risk:EthnicDiscrimination](https://w3id.org/lmodel/dpv/risk/EthnicDiscrimination)





```mermaid
 classDiagram
    class EthnicDiscrimination
    click EthnicDiscrimination href "../EthnicDiscrimination/"
      PotentialConsequence <|-- EthnicDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- EthnicDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- EthnicDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Racism <|-- EthnicDiscrimination
        click Racism href "../Racism/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Racism](Racism.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **EthnicDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:EthnicDiscrimination](https://w3id.org/lmodel/dpv/risk/EthnicDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Ethnic Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#EthnicDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:EthnicDiscrimination |
| native | risk:EthnicDiscrimination |
| exact | dpv_risk:EthnicDiscrimination, dpv_risk_owl:EthnicDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EthnicDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EthnicDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination against individuals based on their ethnicity or cultural

  heritage'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Ethnic Discrimination
exact_mappings:
- dpv_risk:EthnicDiscrimination
- dpv_risk_owl:EthnicDiscrimination
is_a: Racism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:EthnicDiscrimination

```
</details>

### Induced

<details>
```yaml
name: EthnicDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#EthnicDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination against individuals based on their ethnicity or cultural

  heritage'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Ethnic Discrimination
exact_mappings:
- dpv_risk:EthnicDiscrimination
- dpv_risk_owl:EthnicDiscrimination
is_a: Racism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:EthnicDiscrimination

```
</details></div>