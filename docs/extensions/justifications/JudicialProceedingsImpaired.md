---
search:
  boost: 10.0
---

# Class: JudicialProceedingsImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the protection of judicial_

_independence and proceedings_



<div data-search-exclude markdown="1">



URI: [justifications:JudicialProceedingsImpaired](https://w3id.org/lmodel/dpv/justifications/JudicialProceedingsImpaired)





```mermaid
 classDiagram
    class JudicialProceedingsImpaired
    click JudicialProceedingsImpaired href "../JudicialProceedingsImpaired/"
      LegalProcessImpaired <|-- JudicialProceedingsImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **JudicialProceedingsImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:JudicialProceedingsImpaired](https://w3id.org/lmodel/dpv/justifications/JudicialProceedingsImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Judicial Proceedings Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#JudicialProceedingsImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:JudicialProceedingsImpaired |
| native | justifications:JudicialProceedingsImpaired |
| exact | dpv_justifications:JudicialProceedingsImpaired, dpv_justifications_owl:JudicialProceedingsImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: JudicialProceedingsImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#JudicialProceedingsImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the protection of judicial

  independence and proceedings'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Judicial Proceedings Impaired
exact_mappings:
- dpv_justifications:JudicialProceedingsImpaired
- dpv_justifications_owl:JudicialProceedingsImpaired
is_a: LegalProcessImpaired
class_uri: justifications:JudicialProceedingsImpaired

```
</details>

### Induced

<details>
```yaml
name: JudicialProceedingsImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#JudicialProceedingsImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the protection of judicial

  independence and proceedings'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Judicial Proceedings Impaired
exact_mappings:
- dpv_justifications:JudicialProceedingsImpaired
- dpv_justifications_owl:JudicialProceedingsImpaired
is_a: LegalProcessImpaired
class_uri: justifications:JudicialProceedingsImpaired

```
</details></div>