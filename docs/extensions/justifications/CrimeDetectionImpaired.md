---
search:
  boost: 10.0
---

# Class: CrimeDetectionImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the detection of criminal_

_offences_



<div data-search-exclude markdown="1">



URI: [justifications:CrimeDetectionImpaired](https://w3id.org/lmodel/dpv/justifications/CrimeDetectionImpaired)





```mermaid
 classDiagram
    class CrimeDetectionImpaired
    click CrimeDetectionImpaired href "../CrimeDetectionImpaired/"
      SecurityImpaired <|-- CrimeDetectionImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- CrimeDetectionImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **CrimeDetectionImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:CrimeDetectionImpaired](https://w3id.org/lmodel/dpv/justifications/CrimeDetectionImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Crime Detection Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#CrimeDetectionImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:CrimeDetectionImpaired |
| native | justifications:CrimeDetectionImpaired |
| exact | dpv_justifications:CrimeDetectionImpaired, dpv_justifications_owl:CrimeDetectionImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrimeDetectionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimeDetectionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the detection of criminal

  offences'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Detection Impaired
exact_mappings:
- dpv_justifications:CrimeDetectionImpaired
- dpv_justifications_owl:CrimeDetectionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimeDetectionImpaired

```
</details>

### Induced

<details>
```yaml
name: CrimeDetectionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimeDetectionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the detection of criminal

  offences'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Detection Impaired
exact_mappings:
- dpv_justifications:CrimeDetectionImpaired
- dpv_justifications_owl:CrimeDetectionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimeDetectionImpaired

```
</details></div>