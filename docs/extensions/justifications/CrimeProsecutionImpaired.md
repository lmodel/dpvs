---
search:
  boost: 10.0
---

# Class: CrimeProsecutionImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the prosecution of criminal_

_offences_



<div data-search-exclude markdown="1">



URI: [justifications:CrimeProsecutionImpaired](https://w3id.org/lmodel/dpv/justifications/CrimeProsecutionImpaired)





```mermaid
 classDiagram
    class CrimeProsecutionImpaired
    click CrimeProsecutionImpaired href "../CrimeProsecutionImpaired/"
      SecurityImpaired <|-- CrimeProsecutionImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- CrimeProsecutionImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **CrimeProsecutionImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:CrimeProsecutionImpaired](https://w3id.org/lmodel/dpv/justifications/CrimeProsecutionImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Crime Prosecution Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#CrimeProsecutionImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:CrimeProsecutionImpaired |
| native | justifications:CrimeProsecutionImpaired |
| exact | dpv_justifications:CrimeProsecutionImpaired, dpv_justifications_owl:CrimeProsecutionImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrimeProsecutionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimeProsecutionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the prosecution of criminal

  offences'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Prosecution Impaired
exact_mappings:
- dpv_justifications:CrimeProsecutionImpaired
- dpv_justifications_owl:CrimeProsecutionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimeProsecutionImpaired

```
</details>

### Induced

<details>
```yaml
name: CrimeProsecutionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimeProsecutionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the prosecution of criminal

  offences'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Prosecution Impaired
exact_mappings:
- dpv_justifications:CrimeProsecutionImpaired
- dpv_justifications_owl:CrimeProsecutionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimeProsecutionImpaired

```
</details></div>