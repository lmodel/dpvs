---
search:
  boost: 10.0
---

# Class: CrimeInvestigationImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the investigation of criminal_

_offences_



<div data-search-exclude markdown="1">



URI: [justifications:CrimeInvestigationImpaired](https://w3id.org/lmodel/dpv/justifications/CrimeInvestigationImpaired)





```mermaid
 classDiagram
    class CrimeInvestigationImpaired
    click CrimeInvestigationImpaired href "../CrimeInvestigationImpaired/"
      SecurityImpaired <|-- CrimeInvestigationImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- CrimeInvestigationImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **CrimeInvestigationImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:CrimeInvestigationImpaired](https://w3id.org/lmodel/dpv/justifications/CrimeInvestigationImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Crime Investigation Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#CrimeInvestigationImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:CrimeInvestigationImpaired |
| native | justifications:CrimeInvestigationImpaired |
| exact | dpv_justifications:CrimeInvestigationImpaired, dpv_justifications_owl:CrimeInvestigationImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrimeInvestigationImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimeInvestigationImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the investigation of criminal

  offences'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Investigation Impaired
exact_mappings:
- dpv_justifications:CrimeInvestigationImpaired
- dpv_justifications_owl:CrimeInvestigationImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimeInvestigationImpaired

```
</details>

### Induced

<details>
```yaml
name: CrimeInvestigationImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimeInvestigationImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the investigation of criminal

  offences'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Investigation Impaired
exact_mappings:
- dpv_justifications:CrimeInvestigationImpaired
- dpv_justifications_owl:CrimeInvestigationImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimeInvestigationImpaired

```
</details></div>