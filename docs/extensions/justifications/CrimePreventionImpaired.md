---
search:
  boost: 10.0
---

# Class: CrimePreventionImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the prevention of criminal_

_offences_



<div data-search-exclude markdown="1">



URI: [justifications:CrimePreventionImpaired](https://w3id.org/lmodel/dpv/justifications/CrimePreventionImpaired)





```mermaid
 classDiagram
    class CrimePreventionImpaired
    click CrimePreventionImpaired href "../CrimePreventionImpaired/"
      SecurityImpaired <|-- CrimePreventionImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- CrimePreventionImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **CrimePreventionImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:CrimePreventionImpaired](https://w3id.org/lmodel/dpv/justifications/CrimePreventionImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Crime Prevention Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#CrimePreventionImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:CrimePreventionImpaired |
| native | justifications:CrimePreventionImpaired |
| exact | dpv_justifications:CrimePreventionImpaired, dpv_justifications_owl:CrimePreventionImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrimePreventionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimePreventionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the prevention of criminal

  offences'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Prevention Impaired
exact_mappings:
- dpv_justifications:CrimePreventionImpaired
- dpv_justifications_owl:CrimePreventionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimePreventionImpaired

```
</details>

### Induced

<details>
```yaml
name: CrimePreventionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimePreventionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the prevention of criminal

  offences'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Prevention Impaired
exact_mappings:
- dpv_justifications:CrimePreventionImpaired
- dpv_justifications_owl:CrimePreventionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimePreventionImpaired

```
</details></div>