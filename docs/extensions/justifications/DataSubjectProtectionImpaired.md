---
search:
  boost: 10.0
---

# Class: DataSubjectProtectionImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the protection of the data_

_subject_



<div data-search-exclude markdown="1">



URI: [justifications:DataSubjectProtectionImpaired](https://w3id.org/lmodel/dpv/justifications/DataSubjectProtectionImpaired)





```mermaid
 classDiagram
    class DataSubjectProtectionImpaired
    click DataSubjectProtectionImpaired href "../DataSubjectProtectionImpaired/"
      SecurityImpaired <|-- DataSubjectProtectionImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- DataSubjectProtectionImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **DataSubjectProtectionImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:DataSubjectProtectionImpaired](https://w3id.org/lmodel/dpv/justifications/DataSubjectProtectionImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Data Subject Protection Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#DataSubjectProtectionImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:DataSubjectProtectionImpaired |
| native | justifications:DataSubjectProtectionImpaired |
| exact | dpv_justifications:DataSubjectProtectionImpaired, dpv_justifications_owl:DataSubjectProtectionImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataSubjectProtectionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#DataSubjectProtectionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the protection of the data

  subject'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Data Subject Protection Impaired
exact_mappings:
- dpv_justifications:DataSubjectProtectionImpaired
- dpv_justifications_owl:DataSubjectProtectionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:DataSubjectProtectionImpaired

```
</details>

### Induced

<details>
```yaml
name: DataSubjectProtectionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#DataSubjectProtectionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the protection of the data

  subject'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Data Subject Protection Impaired
exact_mappings:
- dpv_justifications:DataSubjectProtectionImpaired
- dpv_justifications_owl:DataSubjectProtectionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:DataSubjectProtectionImpaired

```
</details></div>