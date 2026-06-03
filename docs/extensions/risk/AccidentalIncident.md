---
search:
  boost: 10.0
---

# Class: AccidentalIncident 


_Incident caused due to accidental actions arising from human or_

_human-controlled situations_



<div data-search-exclude markdown="1">



URI: [risk:AccidentalIncident](https://w3id.org/lmodel/dpv/risk/AccidentalIncident)





```mermaid
 classDiagram
    class AccidentalIncident
    click AccidentalIncident href "../AccidentalIncident/"
      Incident <|-- AccidentalIncident
        click Incident href "../Incident/"
      
      
```





## Inheritance
* [Incident](Incident.md)
    * **AccidentalIncident**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AccidentalIncident](https://w3id.org/lmodel/dpv/risk/AccidentalIncident) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Accidental Incident




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AccidentalIncident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AccidentalIncident |
| native | risk:AccidentalIncident |
| exact | dpv_risk:AccidentalIncident, dpv_risk_owl:AccidentalIncident |
| close | iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AccidentalIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccidentalIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Incident caused due to accidental actions arising from human or

  human-controlled situations'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accidental Incident
exact_mappings:
- dpv_risk:AccidentalIncident
- dpv_risk_owl:AccidentalIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:AccidentalIncident

```
</details>

### Induced

<details>
```yaml
name: AccidentalIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AccidentalIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Incident caused due to accidental actions arising from human or

  human-controlled situations'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Accidental Incident
exact_mappings:
- dpv_risk:AccidentalIncident
- dpv_risk_owl:AccidentalIncident
close_mappings:
- iso42001:AIIncident
is_a: Incident
class_uri: risk:AccidentalIncident

```
</details></div>